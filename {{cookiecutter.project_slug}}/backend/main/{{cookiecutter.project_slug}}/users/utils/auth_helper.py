# google
from google.auth.transport import requests as google_requests
from google.oauth2 import id_token
# rest framework
from rest_framework_simplejwt.tokens import RefreshToken


class UserToken:
    @staticmethod
    def get_token(user):
        token = RefreshToken.for_user(user)

        return {
            "refresh_token": str(token),
            "access_token": str(token.access_token),
        }


class GoogleOAuth:
    @staticmethod
    def validate_google_token(token, client_id):
        try:
            id_info = id_token.verify_oauth2_token(
                token, google_requests.Request(), client_id
            )

            if id_info["iss"] not in [
                "accounts.google.com",
                "https://accounts.google.com",
            ]:
                return None

            data = {
                "email": id_info["email"],
                "username": id_info["email"].split("@")[0],
            }

            return data

        except ValueError as e:
            print(f"Except caught: {e}")
            return None
