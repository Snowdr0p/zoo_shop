from django import forms
from .validators import validate_phone_number


class ReviewForm(forms.Form):
    """form for a review"""
    name = forms.CharField(label='Имя', max_length=100, help_text='Иванов Иван')
    phone_number = forms.CharField(
        label='Телефонный номер',
        max_length=20,
        validators=[validate_phone_number],
        help_text='+375 (xx) xxx-xx-xx',
    )
    pet_name = forms.CharField(label='Имя питомца', max_length=20, help_text='Лесиния')
    text = forms.CharField(label='Отзыв', max_length=200, widget=forms.Textarea(attrs={
        'rows': 4,
        'cols': 60,
        'style': 'resize: none; width: 100%;',
    }), help_text='Самый лучший магазин.'
    )
