"""
Account APIs
Mostafa Rasouli
mostafarasooli54@gmail.com
August 2024
"""

from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from rest_framework_simplejwt.tokens import RefreshToken

# Local
from accounts.serializers import UserSerializer, UserAuthSerializer
from accounts.models import UserAuthentication
from utils.response import get_response
from utils.auth import get_auth_token
from utils.messages import Message


class UserLoginAPI(APIView):
    serializer_class = UserAuthSerializer
    response_serializer_class = UserSerializer

    def post(self, request):
        data = request.data
        srz = self.serializer_class(data=data)

        if srz.is_valid():
            vd = srz.validated_data
            user = authenticate(request, username=vd['username'], password=vd['password'])

            if user:
                return get_response({'auth': get_auth_token(user), 'user': self.response_serializer_class(user).data})

            UserAuthentication.objects.create(username=data['username'])
            return get_response(errors={'detail': Message.ERR_USER_NOT_FOUND})

        return get_response(errors=srz.errors)


class UserRefreshLoginAPI(APIView):
    permission_classes = []

    def post(self, request):
        refresh_token = request.data.get('refresh_token')

        if not refresh_token:
            return get_response(errors={'detail': Message.ER_REFRESH_TOKEN_REQUIRED})

        try:
            refresh = RefreshToken(refresh_token)
            data = {'access': str(refresh.access_token)}

            return get_response(data)

        except InvalidToken:
            return get_response(errors={'detail': Message.ERR_REFRESH_TOKEN_INVALID})
        except TokenError as e:
            return get_response(errors={'detail': str(e)})
        except Exception:
            return get_response(errors={'detail': Message.ERR_TRY})

