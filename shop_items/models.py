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
    img = models.ImageField(
        verbose_name="Изображение бренда", upload_to="items/brands/", blank=True, null=True
    )
    show_popular = models.BooleanField(verbose_name="Показывать в популярных", default=True, db_index=True)

    def __str__(self) -> str:
        return f"{self.name}"
    
    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'
    

class Item(models.Model):
    """Shop item"""
    name = models.CharField(verbose_name='Название товара', max_length=200)
    img = models.ImageField(
        verbose_name='Изображение товара', upload_to='items/', blank=True, null=True
    )
    brand = models.ForeignKey(
        Brand, verbose_name='Бренд', default=None, null=True, blank=True, on_delete=models.SET_NULL
    )

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

class MeasuredItem(models.Model):
    """Cost and measure of an item"""
    KILOGRAMS = 'кг'
    GRAMS = 'г'
    LITERS = 'л'
    AMOUNT = 'шт'

    TYPE_CHOICES = [
        (KILOGRAMS, 'Килограммы'),
        (GRAMS, 'Граммы'),
        (LITERS, 'Литры'),
        (AMOUNT, 'штуки'),
    ]

    measurment_type = models.CharField(
        verbose_name='Единица измерения', max_length=2, choices=TYPE_CHOICES, default=KILOGRAMS
    )
    amount = models.IntegerField(verbose_name='Количество в единицах измерения', default=0)
    cost = models.DecimalField(verbose_name='Цена товара', max_digits=8, decimal_places=2, default=0)
    item = models.ForeignKey(Item, verbose_name='Товар', on_delete=models.CASCADE)
    items_amount = models.PositiveIntegerField(verbose_name='Количество единиц товара на складе', default=0)

    def __str__(self) -> str:
        return f"{self.amount} {self.measurment_type}"

    class Meta:
        verbose_name = 'Цена за единицу товара'
        verbose_name_plural = 'Цены за единицу товара'
