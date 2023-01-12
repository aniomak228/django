from .models import Articles
from django.forms import ModelForm, TextInput, Textarea, FileInput


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'anons', 'text', 'img']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Назва'
            }),
            'anons': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Анонс'
            }),
            'img': FileInput(attrs={
                'class': 'form-control',
                'placeholder': 'Картинка'
            }),
            'text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст'
            }),
        }