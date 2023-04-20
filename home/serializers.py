from rest_framework import serializers

from .models import *


# Serializers define the API representation.
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class BrandsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brands
        fields = "__all__"
