# Generated by Django 4.1.5 on 2023-01-11 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Назва')),
                ('anons', models.CharField(max_length=250, verbose_name='Анонс')),
                ('text', models.TextField(verbose_name='Текст')),
                ('date', models.DateTimeField(verbose_name='Дата публікації')),
            ],
        ),
    ]