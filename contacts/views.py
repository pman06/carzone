from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact
from users.models import CustomUser
from .tasks import send_admin_mail_task, send_user_confirm_mail_task
# Create your views here.
def inquiry(request):
    if request.method == "POST":
        car_id = request.POST['car_id']
        car_title = request.POST['car_title']
        user_id = request.POST['user_id']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        customer_need = request.POST['customer_need']
        city = request.POST['city']
        state = request.POST['state']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

    if request.user.is_authenticated:
        has_contacted = Contact.objects.filter(user_id=user_id, car_id=car_id).exists()

    if has_contacted:
        messages.error(request, 'You have already made an enquiry about this car. Please check your Dashboard')
        return redirect('cars:car_detail', id=car_id)

    contact = Contact(car_id=car_id,car_title=car_title, user_id=user_id,
        first_name=first_name, last_name=last_name, customer_need=customer_need,
        city=city, state=state, email=email, phone=phone, message=message)
    contact.save()

    admin_info =  CustomUser.objects.get(is_superuser=True)
    admin_email = admin_info.email
    send_admin_mail_task.delay(admin_email, car_title)
    send_user_confirm_mail_task.delay(email, car_title)
    messages.success(request, 'Your request has been successfully submitted, we will get back to you shortly')

    # call send mail task

    return redirect('cars:car_detail', id=car_id)
