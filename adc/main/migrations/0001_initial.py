# Generated by Django 4.1.7 on 2023-04-26 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cases',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Найменування')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('preview', models.CharField(max_length=255, verbose_name='Короткий текст')),
                ('content', models.TextField(blank=True, verbose_name='Повний текст')),
                ('photo', models.ImageField(upload_to='', verbose_name='Фотографія')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Дата створення')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Дата оновлення')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опублікування')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Найменування')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('preview', models.CharField(max_length=255, verbose_name='Короткий текст')),
                ('content', models.TextField(blank=True, verbose_name='Повний текст')),
                ('photo', models.ImageField(upload_to='', verbose_name='Фотографія')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Дата створення')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Дата оновлення')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опублікування')),
            ],
        ),
    ]
