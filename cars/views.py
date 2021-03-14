from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Car
# Create your views here.

def cars(request):
    try:
        cars = Car.objects.all().order_by('-created_date')
        year_search_field = Car.objects.values_list('year', flat=True).distinct()
        city_search_field = Car.objects.values_list('city', flat=True).distinct()
        model_search_field = Car.objects.values_list('model', flat=True).distinct()
        body_style_search_field = Car.objects.values_list('body_style', flat=True).distinct()
    except Car.DoesNotExist:
        pass
    paginator = Paginator(cars, 1)
    page = request.GET.get('page')
    paged_cars = paginator.get_page(page)
    return render(request, 'cars/cars.html', {'section':'cars', 'cars':paged_cars,
                                                                'year_search_field':year_search_field,
                                                                'city_search_field':city_search_field,
                                                                'body_style_search_field':body_style_search_field,
                                                                'model_search_field':model_search_field})


def car_details(request, id):
    car = get_object_or_404(Car, id=id)

    return render(request,'cars/car_details.html', {'car':car})

def search(request):
    result = Car.objects.order_by('-created_date')
    year_search_field = Car.objects.values_list('year', flat=True).distinct()
    city_search_field = Car.objects.values_list('city', flat=True).distinct()
    model_search_field = Car.objects.values_list('model', flat=True).distinct()
    body_style_search_field = Car.objects.values_list('body_style', flat=True).distinct()
    transmission_search_field = Car.objects.values_list('transmission', flat=True).distinct()

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            try:
                result = result.filter(description__icontains=keyword)
            except Car.DoesNotExist:
                pass

    if 'model' in request.GET:
        model = request.GET['model']
        if model:
            try:
                result = result.filter(model__iexact=model)
            except Car.DoesNotExist:
                pass

    if 'body-style' in request.GET:
        body_style = request.GET['body-style']
        if body_style:
            try:
                result = result.filter(body_style__iexact=body_style)
            except Car.DoesNotExist:
                pass

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            try:
                result = result.filter(city__iexact=city)
            except Car.DoesNotExist:
                pass

    if 'year' in request.GET:
        year = request.GET['year']
        if year:
            try:
                result = result.filter(year__iexact=year)
            except Car.DoesNotExist:
                pass
    if 'transmission' in request.GET:
        transmission = request.GET['transmission']
        if transmission:
            try:
                result = result.filter(transmission__iexact=transmission)
            except Car.DoesNotExist:
                pass

    if 'min_price' in request.GET:
        min_price = request.GET['min_price']
        max_price = request.GET['max_price']
        if min_price:
            try:
                result = result.filter(price__gte=min_price, price__lte=max_price)
            except Car.DoesNotExist:
                pass
    return render(request, 'cars/search.html', {'result':result,'year_search_field':year_search_field,
                                                        'city_search_field':city_search_field,
                                                        'body_style_search_field':body_style_search_field,
                                                        'model_search_field':model_search_field,
                                                        'transmission_search_field':transmission_search_field})
