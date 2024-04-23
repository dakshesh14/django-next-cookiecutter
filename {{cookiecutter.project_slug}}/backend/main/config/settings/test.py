# """
# With these settings, tests run faster.
# """

# from .base import *  # noqa
# from .base import env

# # GENERAL
# # ------------------------------------------------------------------------------
# # https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# SECRET_KEY = env(
#     "DJANGO_SECRET_KEY",
#     default="NTP5HDo0bmXwsRfx5LpU9Mm9QBlVKwZW5YLgAZrj3YeZKtdZdrHITKQVPdu0csD4",
# )
# # https://docs.djangoproject.com/en/dev/ref/settings/#test-runner
# TEST_RUNNER = "django.test.runner.DiscoverRunner"

# # PASSWORDS
# # ------------------------------------------------------------------------------
# # https://docs.djangoproject.com/en/dev/ref/settings/#password-hashers
# PASSWORD_HASHERS = ["django.contrib.auth.hashers.MD5PasswordHasher"]

# # EMAIL
# # ------------------------------------------------------------------------------
# # https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
# EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"

# # DEBUGGING FOR TEMPLATES
# # ------------------------------------------------------------------------------
# TEMPLATES[0]["OPTIONS"]["debug"] = True  # type: ignore # noqa: F405

# # MEDIA
# # ------------------------------------------------------------------------------
# # https://docs.djangoproject.com/en/dev/ref/settings/#media-url
# MEDIA_URL = "http://media.testserver"
# # Your stuff...
# # ------------------------------------------------------------------------------
