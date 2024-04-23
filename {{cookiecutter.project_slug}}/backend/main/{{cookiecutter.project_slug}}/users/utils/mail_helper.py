from {{cookiecutter.project_slug}}.users.tasks import send_email
from django.template.loader import render_to_string


def send_magic_link_email(request, email, token):
    subject = "Login to your account"
    html_content = render_to_string(
        "users/magic_link_email.html",
        {
            "email": email,
            "token": token,
            "domain": request.get_host(),
            "magic_link_url": f"{request.scheme}://{request.get_host()}/users/magic-link/?token={token}",
        },
    )
    send_email.delay(subject, html_content, email)
    return True
