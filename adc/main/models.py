from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField

class Product(models.Model):
    title = models.CharField(max_length=255, verbose_name="Найменування")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    preview = models.TextField(max_length=500, verbose_name="Короткий текст")
    content = RichTextField(blank=True, verbose_name="Повний текст")
    photo = models.ImageField(verbose_name="Фотографія")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата створення")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Дата оновлення")
    is_published = models.BooleanField(default=True, verbose_name="Опублікування")

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('post', kwards={'post_slug': self.slug})

class Cases(models.Model):
    title = models.CharField(max_length=255, verbose_name="Найменування")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    preview = models.CharField(max_length=255, verbose_name="Короткий текст")
    content = RichTextField(blank=True, verbose_name="Повний текст")
    photo = models.ImageField(verbose_name="Фотографія")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата створення")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Дата оновлення")
    is_published = models.BooleanField(default=True, verbose_name="Опублікування")

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('post', kwards={'post_slug': self.slug})
# class News(models.Model):
#     title = models.CharField(max_length=255, verbose_name="Найменування")
#     slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
#     preview = models.CharField(max_length=255, verbose_name="Короткий текст")
#     content = models.TextField(blank=True, verbose_name="Повний текст")
#     photo = models.ImageField(verbose_name="Фотографія")
#     time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата створення")
#     time_update = models.DateTimeField(auto_now=True, verbose_name="Дата оновлення")
#     is_published = models.BooleanField(default=True, verbose_name="Опублікування")
#
#     def __str__(self):
#         return self.title
#     def get_absolute_url(self):
#         return reverse('post', kwards={'post_slug': self.slug})

