# Generated by Django 4.1.7 on 2023-04-17 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_remove_subcategory_pic_remove_subcategory_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='specification',
            field=models.CharField(default='specfication is dynamic', max_length=300),
        ),
    ]
