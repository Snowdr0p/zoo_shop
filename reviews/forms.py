from django import forms
from .validators import validate_phone_number


class ReviewForm(forms.Form):
    """form for a review"""
    name = forms.CharField(label='Имя', max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))
    phone_number = forms.CharField(
        label='Телефонный номер',
        max_length=19,
        validators=[validate_phone_number],
        widget=forms.TextInput(attrs={
            'class': 'form-control',
        })
    )
    pet_name = forms.CharField(label='Имя питомца', max_length=20,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
    }))
    text = forms.CharField(label='Отзыв', max_length=200, widget=forms.Textarea(attrs={
        'rows': 4,
        'cols': 60,
        'style': 'resize: none;',
        'class': 'form-control',
    })
    )
