from django.shortcuts import render
from .models import Team
# Create your views here.

def home(request):
    try:
        teams = Team.objects.all()
    except Team.DoesNotExist:
        pass
    return render(request, "pages/home.html", {'teams':teams})

def about(request):
    try:
        team = Team.objects.all()
    except Team.DoesNotExist:
        pass
    return render(request, 'pages/about.html', {'teams':team})

def services(request):
    return render(request, 'pages/services.html')

def contact(request):
    return render(request, "pages/contact.html")
