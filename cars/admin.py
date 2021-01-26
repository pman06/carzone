from django.contrib import admin
from .models import Car
# Register your models here.
@admin.register(Car)
class CarADmin(admin.ModelAdmin):
    list_display = ['car_title', 'created_date']
# admin.site.register(Car)
