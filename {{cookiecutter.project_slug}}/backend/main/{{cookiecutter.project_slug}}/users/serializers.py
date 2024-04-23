from django.contrib.auth import authenticate, get_user_model

# rest framework
from rest_framework import serializers

# utils
from .utils.auth_helper import GoogleOAuth

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
        )


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password",
        )
        extra_kwargs = {
            "password": {"write_only": True},
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, attrs):
        user = authenticate(**attrs)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")


class GoogleLoginSerializer(serializers.Serializer):
    credential = serializers.CharField()
    client_id = serializers.CharField()

    def validate(self, attrs):
        token = attrs.get("credential")
        client_id = attrs.get("client_id")

        id_info = GoogleOAuth.validate_google_token(token, client_id)

        email = id_info.get("email", None) if id_info else None

        if not id_info or not email:
            raise serializers.ValidationError(
                {
                    "message": "We could not verify your Google Account. Please try again.",
                }
            )

        user, created = User.objects.get_or_create(
            email=email,
        )

        if created:
            user.username = id_info.get("username")
            user.first_name = id_info.get("first_name")
            user.last_name = id_info.get("last_name")

            user.set_unusable_password()
            user.save()

        return user
