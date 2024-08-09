"""
Account serializers
Mostafa Rasouli
mostafarasooli54@gmail.com
August 2024
"""

from datetime import timedelta
from django.utils import timezone
from rest_framework import serializers
from django.contrib.auth.models import User

# Local
from accounts.models import UserAuthentication
from utils.messages import Message


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password', 'groups', 'user_permissions')


class UserAuthSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        username = attrs.get('username')

        # Check if spam request
        exp_time = timezone.now() - timedelta(minutes=2)
        if UserAuthentication.objects.filter(username=username, used_at__isnull=True,
                                             date__gte=exp_time).count() >= 3:
            raise serializers.ValidationError({'detail': Message.ERR_SPAM_AUTH_REQUEST})

        return attrs
