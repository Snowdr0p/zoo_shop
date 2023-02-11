"""Admin panel config for shop_items"""
from django.contrib import admin
from . import models


@admin.register(models.Animal)
class AnimalAdmin(admin.ModelAdmin):
    """config class for Animal model"""
    list_display = ('id', 'name', 'img', 'thumbnail_preview')
    list_editable = ('name', 'img')

    def thumbnail_preview(self, obj):
        """thumbnail for animal"""
        return obj.thumbnail_preview
    
    thumbnail_preview.short_description = 'Предпросмотр изображения'
    thumbnail_preview.allow_tags = True


@admin.register(models.ItemType)
class ItemTypeAdmin(admin.ModelAdmin):
    """config class for ItemType"""
    list_display = ['id', 'name', 'animal']
    list_editable = ['name', 'animal']


@admin.register(models.Brand)
class BrandAdmin(admin.ModelAdmin):
    """config class for Brand model"""
    list_display = ['id', 'name', 'img']
    list_editable = ['name', 'img']
