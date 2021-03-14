from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Team, BusinessInfo
from .tasks import contact_email_task
from cars.models import Car
from users.models import CustomUser
# Create your views here.

def home(request):
    try:
        latest_cars = Car.objects.all().order_by('-created_date')
        featured_cars = Car.featured.all()
        teams = Team.objects.all()
        biz_info = BusinessInfo.objects.first()
        # search_fields = Car.objects.values('year','body_style', 'city', 'model').order_by('-created_date').distinct()
        year_search_field = Car.objects.values_list('year', flat=True).distinct()
        city_search_field = Car.objects.values_list('city', flat=True).distinct()
        model_search_field = Car.objects.values_list('model', flat=True).distinct()
        body_style_search_field = Car.objects.values_list('body_style', flat=True).distinct()

    except Team.DoesNotExist:
        pass
    except BusinessInfo.DoesNotExist:
        pass
    except Car.DoesNotExist:
        pass
    return render(request, "pages/home.html", {'teams':teams, 'biz_info':biz_info,
                                                'section':'home', 'featured_cars':featured_cars,
                                                'latest_cars':latest_cars,
                                                'year_search_field':year_search_field,
                                                'city_search_field':city_search_field,
                                                'body_style_search_field':body_style_search_field,
                                                'model_search_field':model_search_field})

def about(request):
    try:
        team = Team.objects.all()
    except Team.DoesNotExist:
        pass
    return render(request, 'pages/about.html', {'teams':team, 'section':'about'})

def services(request):
    return render(request, 'pages/services.html', {'section':'service'})

def contact(request):
    biz_info = BusinessInfo.objects.first()
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        phone = request.POST['phone']
        message = request.POST['message']

        message_body = 'Name: '+name+ '. \nEmail: '+email+ '. \nPhone: '+phone+'. \nSubject: '+subject+ '. \nMessage: ' +message
        email_subject = 'New message on Carzone about: '+subject
        admin_info =  CustomUser.objects.get(is_superuser=True)
        admin_email = admin_info.email
        contact_email_task.delay(email_subject,message_body,email,admin_email)
        messages.success(request, 'Thank you for contacting us. We will get back to you shortly')
        return redirect('pages:contact')
    return render(request, "pages/contact.html", {'section':'contact', 'biz_info':biz_info})
