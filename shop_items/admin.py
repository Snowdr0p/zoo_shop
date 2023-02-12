"""Admin panel config for shop_items"""
from django.contrib import admin
from django.utils.safestring import mark_safe
from . import models


@admin.register(models.Animal)
class AnimalAdmin(admin.ModelAdmin):
    """config class for Animal model"""
    list_display = 'id', 'name', 'preview', 'img', 'show'
    readonly_fields = 'preview',
    list_editable = 'name', 'img', 'show'

    def preview(self, obj: models.Animal) -> str:
        """thumbnail for animal"""
        return obj.thumbnail_preview
    
    preview.short_description = 'Предпросмотр изображения'
    preview.allow_tags = True


@admin.register(models.ItemType)
class ItemTypeAdmin(admin.ModelAdmin):
    """config class for ItemType"""
    list_display = 'id', 'name', 'animal'
    list_editable = 'name', 'animal'


@admin.register(models.Brand)
class BrandAdmin(admin.ModelAdmin):
    """config class for Brand model"""
    list_display = 'id', 'name', 'preview', 'img', 'show_popular'
    readonly_fields = 'preview',
    list_editable = 'name', 'img', 'show_popular'

    def preview(self, obj: models.Brand) -> str:
        """preview an image of the obj"""
        if obj.img:
            return mark_safe(f'<img src="{obj.img.url}" alt="{obj.name}" class="animal-img">')
        
        return 'Нет изображения'
    
    preview.short_description = 'Изображение'


class MeasuredItemInline(admin.TabularInline):
    fields = 'cost', 'amount', 'measurment_type', 'items_amount'
    extra = 0
    model = models.MeasuredItem


@admin.register(models.Item)
class ItemAdmin(admin.ModelAdmin):
    """config clas for Item model"""
    list_display = 'id', 'name', 'brand',  'preview', 'img',
    readonly_fields = 'preview',
    list_editable = 'name', 'brand', 'img'
    inlines = MeasuredItemInline,

    def preview(self, obj: models.Item) -> str:
        """preview of and image of the obj"""
        if obj.img:
            return mark_safe(f'<img src="{obj.img.url}" alt="{obj.name}" class="animal-img">')
        
        return 'Нет изображения'

    preview.short_description = 'Изображение'
