from django.db import models
from datetime import datetime
from django.contrib.auth import get_user

class Articles(models.Model):
    title = models.CharField('Назва', max_length=50)
    anons = models.CharField('Анонс', max_length=250)
    text = models.TextField('Текст')
    img = models.ImageField('Картинка', upload_to='', blank=True)
    date = models.DateTimeField(default=datetime.today)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новина'
        verbose_name_plural = 'Новини'