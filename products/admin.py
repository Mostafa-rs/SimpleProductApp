"""
Product admin
Mostafa Rasouli
mostafarasooli54@gmail.com
August 2024
"""

from django.contrib import admin

# Local
from products.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')
