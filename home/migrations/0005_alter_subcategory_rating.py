# Generated by Django 4.1.7 on 2023-04-06 10:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_subcategory_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcategory',
            name='rating',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)]),
        ),
    ]
