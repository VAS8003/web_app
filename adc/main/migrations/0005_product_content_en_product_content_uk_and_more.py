# Generated by Django 4.1.7 on 2023-06-27 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_cases_preview'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='content_en',
            field=models.TextField(blank=True, null=True, verbose_name='Повний текст'),
        ),
        migrations.AddField(
            model_name='product',
            name='content_uk',
            field=models.TextField(blank=True, null=True, verbose_name='Повний текст'),
        ),
        migrations.AddField(
            model_name='product',
            name='preview_en',
            field=models.TextField(max_length=500, null=True, verbose_name='Короткий текст'),
        ),
        migrations.AddField(
            model_name='product',
            name='preview_uk',
            field=models.TextField(max_length=500, null=True, verbose_name='Короткий текст'),
        ),
        migrations.AddField(
            model_name='product',
            name='title_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Найменування'),
        ),
        migrations.AddField(
            model_name='product',
            name='title_uk',
            field=models.CharField(max_length=255, null=True, verbose_name='Найменування'),
        ),
    ]