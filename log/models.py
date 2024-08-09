"""
Log models
Mostafa Rasouli
mostafarasooli54@gmail.com
August 2024
"""

from django.db import models


class Log(models.Model):
    log_type = models.CharField(max_length=100, null=True)
    api = models.TextField(null=True)
    user = models.ForeignKey('auth.User', models.SET_NULL, null=True)
    request = models.TextField(null=True)
    body = models.TextField(null=True)
    log_desc = models.TextField(null=True)
    device = models.TextField(null=True)
    ip = models.CharField(max_length=15, null=True)