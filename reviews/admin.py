from django.contrib import admin
from .models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    """Admin panel configs for Review"""
    list_display = ['id', "name", 'pet_name', "show", "text"]
    list_editable = ['name', 'pet_name', 'show', 'text']
