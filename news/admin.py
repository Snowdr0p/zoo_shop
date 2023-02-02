from django.contrib import admin
from .models import News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    """Admin panel for news"""
    list_display = ['name', 'show', 'pub_date']
    list_editable = ['show']
