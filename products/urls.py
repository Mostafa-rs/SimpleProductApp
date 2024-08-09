"""
Product URLs
Mostafa Rasouli
mostafarasooli54@gmail.com
August 2024
"""

from django.urls import path

# Local
from products import apis


urlpatterns = [
    path('', apis.ProductListCreateAPI.as_view()),
    path('<int:pk>/', apis.ProductRetrieveUpdateDeleteAPI.as_view())
]