from config import celery_app
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags


@celery_app.task()
def send_email(subject, html_content, to):
    try:
        text_content = strip_tags(html_content)
        email = EmailMultiAlternatives(
            subject, text_content, settings.EMAIL_HOST_USER, [to]
        )
        email.attach_alternative(html_content, "text/html")
        email.send()
        return True
    except Exception as e:
        print(e)
        return False
