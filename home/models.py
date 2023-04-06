from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=300)
    pic = models.ImageField(upload_to='images')
    slug = models.CharField(max_length=300)

    def __str__(self):
        return self.name
