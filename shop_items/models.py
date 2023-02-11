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
        return mark_safe(f'<img src="{img_url}" alt="{self.name}" class="animal-img">')


    def __str__(self):
        return f"{self.name}"

    class Meta:
        """Meta class for animal"""
        verbose_name = "Вид животного"
        verbose_name_plural = "Виды животных"


class ItemType(models.Model):
    """Type of an item"""
    name = models.CharField(verbose_name='Тип товара', max_length=20)
    animal = models.ForeignKey(
        Animal, verbose_name='Вид животного', on_delete=models.SET_NULL, blank=True, null=True
    )

    def __str__(self) -> str:
        return f"{self.name} для {self.animal.name}"
    
    class Meta:
        verbose_name = "Тип товара"
        verbose_name_plural = "Типы товаров"


class Brand(models.Model):
    """Brand of an item"""
    name = models.CharField(verbose_name="Название бренда", max_length=20)
    img = models.ImageField(verbose_name="Изображение бренда", upload_to="items/brands/")

    def __str__(self) -> str:
        return f"{self.name}"
    

    
