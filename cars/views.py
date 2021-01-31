from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Car
# Create your views here.

def cars(request):
    try:
        cars = Car.objects.all().order_by('-created_date')
    except Car.DoesNotExist:
        pass
    paginator = Paginator(cars, 8)
    page = request.GET.get('page')
    paged_cars = paginator.get_page(page)
    return render(request, 'cars/cars.html', {'section':'cars', 'cars':paged_cars})


def car_details(request, id):
    car = get_object_or_404(Car, id=id)
    return render(request,'cars/car_details.html', {'car':car})
