# django imports
# local imports
from {{cookiecutter.project_slug}}.users.managers import UserManager
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Default custom user model for {{cookiecutter.project_slug}}.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    username = models.CharField(
        "Username", max_length=150, blank=True, null=True, unique=False
    )
    email = models.EmailField("Email address", unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    objects = UserManager()

    def __str__(self):
        return f"{self.username}"
