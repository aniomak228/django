# Generated by Django 4.1.5 on 2023-01-12 04:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articles',
            options={'verbose_name': 'Новина', 'verbose_name_plural': 'Новини'},
        ),
        migrations.AddField(
            model_name='articles',
            name='img',
            field=models.ImageField(blank=True, upload_to='', verbose_name='Картинка'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.today),
        ),
    ]