from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=300)
    pic = models.ImageField(upload_to='images')
    slug = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=300)
    pic = models.ImageField(upload_to='images')
    slug = models.CharField(max_length=300)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    rating = models.IntegerField(default=1, validators=[
        MaxValueValidator(5),
        MinValueValidator(1)

    ])

    def __str__(self):
        return self.name


class Slider(models.Model):
    name = models.CharField(max_length=300)
    pic = models.ImageField(upload_to='images')
    Header = models.CharField(max_length=300, default="hi")
    SubHeader = models.CharField(max_length=300,default="hi")
    slug = models.CharField(max_length=300)

    def __str__(self):
        return self.name
