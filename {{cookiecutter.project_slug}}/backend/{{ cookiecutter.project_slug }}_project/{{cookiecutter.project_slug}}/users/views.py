import json
import random

from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.cache import cache
from django.core.validators import validate_email

# rest framework
from rest_framework import generics, permissions, status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

# serializers
from .serializers import GoogleLoginSerializer, LoginSerializer, RegisterSerializer, UserSerializer

# utils
from .utils.auth_helper import UserToken
from .utils.mail_helper import send_magic_link_email

User = get_user_model()


class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [
        permissions.AllowAny,
    ]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        # raise exception if serializer is not valid
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        token = UserToken.get_token(user)

        return Response(
            {
                "user": UserSerializer(user, context=self.get_serializer_context()).data,
                "refresh_token": token["refresh_token"],
                "access_token": token["access_token"],
            }
        )


class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer

    permission_classes = [
        permissions.AllowAny,
    ]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data

        token = UserToken.get_token(user)

        return Response(
            {
                "user": UserSerializer(user, context=self.get_serializer_context()).data,
                "refresh_token": token["refresh_token"],
                "access_token": token["access_token"],
            }
        )


class UserAPI(generics.RetrieveUpdateAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = UserSerializer

    def get_object(self):
        # since we are request user, we don't need to use custom permission_classes
        return self.request.user

    def put(self, request: Request) -> Response:
        user = self.get_object()
        serializer = self.get_serializer(user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)


class GoogleOAuthAPI(generics.GenericAPIView):
    permission_classes = [
        permissions.AllowAny,
    ]

    serializer_class = GoogleLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data

        token = UserToken.get_token(user)

        return Response(
            {
                "user": UserSerializer(user, context=self.get_serializer_context()).data,
                "refresh_token": token["refresh_token"],
                "access_token": token["access_token"],
            }
        )


class MagicLinkGenerationAPI(APIView):
    permission_classes = [
        permissions.AllowAny,
    ]

    def post(self, request, *args, **kwargs):
        email = request.data.get("email")

        if not email:
            return Response({"message": "Email is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            validate_email(email)
        except Exception:
            return Response(
                {"message": "Please provide a valid email."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        key = f"magic_link:{email}"

        token = ""
        for _ in range(6):
            token += str(random.randint(0, 9))

        TIMEOUT = 60 * 5  # 5 minutes

        if cache.get(key):
            data = json.loads(cache.get(key))

            if data["attempts"] >= 3:
                return Response(
                    {"message": "Too many attempts. Please wait before trying again."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            data["attempts"] += 1
            data["token"] = token

            cache.set(key, json.dumps(data), timeout=TIMEOUT)

        else:
            data = {
                "attempts": 1,
                "token": token,
            }

            cache.set(key, json.dumps(data), timeout=TIMEOUT)

        send_magic_link_email(request, email, token)

        return Response(
            {
                "message": "Magic link has been sent to your email.",
                "token": token if settings.DEBUG else "",  # for debugging purposes
            },
            status=status.HTTP_200_OK,
        )


class MagicLinkVerificationAPI(APIView):
    permission_classes = [
        permissions.AllowAny,
    ]

    def post(self, request, *args, **kwargs):
        email = request.data.get("email")
        token = request.data.get("token")

        if not email or not token:
            return Response(
                {"message": "Email and token are required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        key = f"magic_link:{email}"

        if not cache.get(key):
            return Response(
                {"message": "Token has expired. Please request a new one."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        data = json.loads(cache.get(key))

        if data["token"] != token:
            return Response({"message": "Invalid token."}, status=status.HTTP_400_BAD_REQUEST)

        # get or create user
        user, created = User.objects.get_or_create(email=email)

        if created:
            user.username = email.split("@")[0]
            user.set_unusable_password()
            user.save()

        token = UserToken.get_token(user)

        return Response(
            {
                "user": UserSerializer(user).data,
                "refresh_token": token["refresh_token"],
                "access_token": token["access_token"],
            }
        )
