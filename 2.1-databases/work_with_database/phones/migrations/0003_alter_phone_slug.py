# Generated by Django 5.0.6 on 2024-06-16 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0002_phone_image_phone_lte_exists_phone_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='slug',
            field=models.SlugField(default=models.CharField(default=None, max_length=50, unique=True, verbose_name='name'), unique=True, verbose_name='slug'),
        ),
    ]