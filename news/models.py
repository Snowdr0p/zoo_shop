from django.db import models
from django.utils.html import mark_safe
from ckeditor_uploader.fields import RichTextUploadingField


class News(models.Model):
    """Новости для сайта"""
    name = models.CharField(verbose_name='Название', max_length=50)
    content = RichTextUploadingField(verbose_name='Содержимое')
    show = models.BooleanField(verbose_name='Показывать на главной', default=True, db_index=True)
    pub_date = models.DateTimeField(verbose_name='Дата добавления', auto_now_add=True, db_index=True)

    def as_html(self) -> str:
        """returns safe html content"""
        return mark_safe(self.content)

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        """Meta class for news"""
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
