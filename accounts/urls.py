"""
Account URls
Mostafa Rasouli
mostafarasooli54@gmail.com
August 2024
"""

from django.urls import path

# Local
from accounts import apis


urlpatterns = [
    path('login/', apis.UserLoginAPI.as_view()),
    path('login/refresh/', apis.UserRefreshLoginAPI.as_view()),
]