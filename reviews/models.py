from django.db import models
from .validators import validate_phone_number
from django.utils import timezone


class Review(models.Model):
    """review model"""
    name = models.CharField(verbose_name="Имя", max_length=50)
    phone_number = models.CharField(
        verbose_name='Телефонный номер',
        max_length=20,
        validators=[validate_phone_number]
    )
    pet_name = models.CharField(verbose_name="Имя питомца", max_length=20)
    text = models.CharField(verbose_name="Отзыв", max_length=200)
    show = models.BooleanField(verbose_name="Отображать отзыв", default=True, db_index=True)
    pub_date = models.DateTimeField(verbose_name="Дата создания отзыва", auto_now_add=True, db_index=True)

    def __str__(self):
        return f"{self.name} ({self.phone_number}: {self.text})"

    class Meta:
        """Meta class for Review"""
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
