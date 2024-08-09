"""
Redis utility functions
Mostafa Rasouli
mostafarasooli54@gmail.com
August 2024
"""

from django.core.cache import cache

# Local
from products.models import Product

class Key:
    PRODUCT_LIST = 'products_list'
    PRODUCT_DETAILS = 'product_details'


def set_cache(key, pk=None):
    data = None

    match key:
        case Key.PRODUCT_LIST:
            data = Product.objects.all()
        case Key.PRODUCT_DETAILS:
            try:
                data = Product.objects.get(pk=pk)
                key = f'{key}_{pk}'
            except Product.DoesNotExist:
                pass

    if data:
        cache.set(key, data, 60*15)

    return data


def get_product_cache(key, pk=None):
    if not pk:
        if not cache.get(key):
            return set_cache(key)
        else:
            return cache.get(key)
    else:
        _key = f'{key}_{pk}'
        if not cache.get(_key):
            return set_cache(key, pk)
        else:
            return cache.get(_key)

