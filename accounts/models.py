"""
Account models
Mostafa Rasouli
mostafarasooli54@gmail.com
August 2024
"""

from django.db import models


class UserAuthentication(models.Model):
    username = models.CharField(max_length=150)
    date = models.DateTimeField(auto_now_add=True)
    used_at = models.DateTimeField(null=True)
