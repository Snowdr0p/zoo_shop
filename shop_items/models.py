"""Model representing shop items"""
from django.db import models
from django.utils.html import mark_safe


class Animal(models.Model):
    """Animal type for item"""
    name = models.CharField(verbose_name='Вид', max_length=20, unique=True, db_index=True)
    img = models.ImageField(verbose_name='Изображение', upload_to="img/animals/")
    show = models.BooleanField(
        verbose_name='Отображение в видах животных', default=True, db_index=True
    )

    @property
    def thumbnail_preview(self):
        img_url = self.img.url
        if img_url is None:
            img_url='#'
        return mark_safe(f'<img src="{img_url}" alt="{self.name}">')


    def __str__(self):
        return f"{self.name}"

    class Meta:
        """Meta class for animal"""
        verbose_name = "Вид животного"
        verbose_name_plural = "Виды животных"


class Category(models.Model):
    """Category of item"""
    name = models.CharField(verbose_name='Название', max_length=20, unique=True, db_index=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        """Meta for category"""
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
