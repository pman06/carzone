from django.shortcuts import render
from .models import Team, BusinessInfo
# Create your views here.

def home(request):
    try:
        teams = Team.objects.all()
        biz_info = BusinessInfo.objects.first()
        # print("Count", BusinessInfo.objects.all().count(), ' \n Bizzname: ',biz_info.email)
    except Team.DoesNotExist:
        pass
    except BusinessInfo.DoesNotExist:
        pass
    return render(request, "pages/home.html", {'teams':teams, 'biz_info':biz_info, 'section':'home'})

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
