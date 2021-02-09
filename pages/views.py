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
    return render(request, "pages/contact.html", {'section':'contact'})
