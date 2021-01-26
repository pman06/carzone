from django.contrib import admin
from .models import Team, BusinessInfo
from django.utils.html import format_html
# Register your models here.
@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):

    def thumbnail(self, obj):
        url = obj.photo.url
        return format_html("<img src='{}' width:40px height=40px />",url)

    thumbnail.short_description = 'Photo'

    list_display = ['id', 'thumbnail','first_name', 'last_name','designation']
    list_display_links = ['id', 'thumbnail', 'first_name']
    list_filter = ['designation']
    search_fields = ['first_name', 'last_name']


@admin.register(BusinessInfo)
class BusinessInfoAdmin(admin.ModelAdmin):
    #Only one record is allowed to be used in template
    def has_add_permission(self, request):
        # if there's already an entry, do not allow adding
        count = BusinessInfo.objects.all().count()
        if count == 0:
          return True

        return False

    list_display= ['business_name','email','phone_number', 'address', 'city', 'country', 'facebook_link']
