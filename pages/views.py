from django.shortcuts import render
from .models import Team, BusinessInfo
from cars.models import Car
# Create your views here.

def home(request):
    try:
        latest_cars = Car.objects.all().order_by('-created_date')
        featured_cars = Car.featured.all()
        teams = Team.objects.all()
        biz_info = BusinessInfo.objects.first()
        # print("Count", BusinessInfo.objects.all().count(), ' \n Bizzname: ',biz_info.email)
    except Team.DoesNotExist:
        pass
    except BusinessInfo.DoesNotExist:
        pass
    except Car.DoesNotExist:
        pass
    return render(request, "pages/home.html", {'teams':teams, 'biz_info':biz_info,
                                                'section':'home', 'featured_cars':featured_cars,
                                                'latest_cars':latest_cars})

def about(request):
    try:
        team = Team.objects.all()
    except Team.DoesNotExist:
        pass
    return render(request, 'pages/about.html', {'teams':team, 'section':'about'})

def services(request):
    return render(request, 'pages/services.html', {'section':'service'})

def contact(request):
    return render(request, "pages/contact.html", {'section':'contact'})
