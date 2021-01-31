from django.urls import path
from . import views

app_name = 'cars'

urlpatterns=[
    path('', views.cars, name='cars'),
    path('<int:id>/', views.car_details, name='car_detail'),
]
