from django.core.mail import send_mail
from celery import task
from django.conf import settings

@task
def contact_email_task(email_subject,message_body,email,admin_email):
    mail_sent =send_mail(
        email_subject,
        message_body,
        settings.EMAIL_HOST_USER,
        [admin_email],
        fail_silently=False,
    )
    return mail_sent
