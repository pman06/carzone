from django.core.mail import send_mail

from celery import task

@task
def send_admin_mail_task(admin_email, car_title):
    mail_sent = send_mail(
        'New Car Inquiry',
        'You have a new Car inquiry on carzone.com, for the listed '+ car_title +'. Please login  to admin page for more information.',
        'myemail@yahoo.com',
        [admin_email],)
    return mail_sent

@task
def send_user_confirm_mail_task(email, car_title):
    mail_sent = send_mail(
        'Confirmation of Inquiry',
        'A new enquiry was submitted carzone.com from your profile, for the listed '+ car_title +'. Please login  to dashboard page for a response from admin.',
        'myemail@yahoo.com',
        [email],)
    return mail_sent
