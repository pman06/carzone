from django.contrib import admin
from .models import Car
from django.utils.html import format_html
# Register your models here.
@admin.register(Car)
class CarADmin(admin.ModelAdmin):

    def thumbnail(self, obj):
        url = obj.car_photo_1.url
        return format_html('<img src="{}" width=40 />',url)
    thumbnail.short_description = 'Photo'

    list_display = ['thumbnail','car_title', 'city', 'color','model','year','body_style', 'created_date', 'is_featured']
    list_display_links = ['car_title']
    list_filter = ['is_featured', 'city', 'body_style']
    list_editable = ['is_featured']
    search_fields = ['car_title', 'city', 'body_style']
