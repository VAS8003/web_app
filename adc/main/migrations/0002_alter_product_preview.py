# Generated by Django 4.1.7 on 2023-05-03 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='preview',
            field=models.TextField(max_length=500, verbose_name='Короткий текст'),
        ),
    ]
