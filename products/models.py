"""
Product models
Mostafa Rasouli
mostafarasooli54@gmail.com
August 2024
"""

from django.core.cache import cache
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=11, decimal_places=2)
    stock = models.PositiveSmallIntegerField(default=0)

    def save(self, *args, **kwargs):
        cache.set(f'product_details_{self.pk}', self, 60*15)

        super().save(*args, **kwargs)
