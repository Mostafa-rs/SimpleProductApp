"""
Product serializers
Mostafa Rasouli
mostafarasooli54@gmail.com
August 2024
"""

from rest_framework import serializers

# Local
from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ('id',)
