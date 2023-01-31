"""Admin panel config for shop_items"""
from django.contrib import admin
from . import models


@admin.register(models.Animal)
class AdminAnimal(admin.ModelAdmin):
    """config class for Animal model"""
    list_display = ('id', 'name', 'img', 'thumbnail_preview')
    list_editable = ('name', 'img')

    def thumbnail_preview(self, obj):
        """thumbnail for animal"""
        return obj.thumbnail_preview
    
    thumbnail_preview.short_description = 'Предпросмотр изображения'
    thumbnail_preview.allow_tags = True
