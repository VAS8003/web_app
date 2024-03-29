# Generated by Django 4.1.7 on 2023-06-28 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_product_content_en_product_content_uk_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cases',
            name='content_en',
            field=models.TextField(blank=True, null=True, verbose_name='Повний текст'),
        ),
        migrations.AddField(
            model_name='cases',
            name='content_uk',
            field=models.TextField(blank=True, null=True, verbose_name='Повний текст'),
        ),
        migrations.AddField(
            model_name='cases',
            name='preview_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Короткий текст'),
        ),
        migrations.AddField(
            model_name='cases',
            name='preview_uk',
            field=models.CharField(max_length=255, null=True, verbose_name='Короткий текст'),
        ),
        migrations.AddField(
            model_name='cases',
            name='title_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Найменування'),
        ),
        migrations.AddField(
            model_name='cases',
            name='title_uk',
            field=models.CharField(max_length=255, null=True, verbose_name='Найменування'),
        ),
    ]
