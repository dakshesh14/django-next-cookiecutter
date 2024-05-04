from django.urls import path

# simple jwt
from rest_framework_simplejwt.views import TokenBlacklistView, TokenRefreshView

from .views import (
    GoogleOAuthAPI,
    LoginAPI,
    MagicLinkGenerationAPI,
    MagicLinkVerificationAPI,
    RegisterAPI,
    UserAPI,
)

app_name = "accounts-api"

urlpatterns = [
    path("login/", LoginAPI.as_view(), name="login"),
    path("register/", RegisterAPI.as_view(), name="register"),
    path("logout/", TokenBlacklistView.as_view(), name="logout"),
    # user related
    path("user/me/", UserAPI.as_view(), name="user"),
    # token related
    path("refresh-token/", TokenRefreshView.as_view(), name="refresh_token"),
    # o-auth
    path("google-login", GoogleOAuthAPI.as_view(), name="google_login"),
    # magic link
    path(
        "magic-link/generate/",
        MagicLinkGenerationAPI.as_view(),
        name="magic-link-generate",
    ),
    path(
        "magic-link/verify/",
        MagicLinkVerificationAPI.as_view(),
        name="magic-link-verify",
    ),
]
