# Generated by Django 4.1.7 on 2023-04-11 13:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_subcategory_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='rating',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)]),
        ),
    ]