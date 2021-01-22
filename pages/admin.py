from django.contrib import admin
from .models import Team
from django.utils.html import format_html
# Register your models here.
@admin.register(Team)
class TeamModel(admin.ModelAdmin):

    def thumbnail(self, obj):
        url = obj.photo.url
        return format_html("<img src='{}' width:40px height=40px />",url)

    thumbnail.short_description = 'Photo'

    list_display = ['id', 'thumbnail','first_name', 'last_name','designation'] 
    list_display_links = ['id', 'thumbnail', 'first_name']
    list_filter = ['designation']
    search_fields = ['first_name', 'last_name']
