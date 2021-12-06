from .models import Articles
from django.forms import ModelForm, TextInput, DateInput
from django import forms



class ArticlesForm(ModelForm, forms.Form, DateInput):
    class Meta:
        model = Articles
        fields = ['title', 'anons', 'full_text', 'data']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название статьи'
            }),
            "anons": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Анонс статьи'
            }),
            "data": DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата публикации',
                'type': 'date'
            }),
            "full_text": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Текст статьи'
            }),

        }