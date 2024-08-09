"""
Custom response
Mostafa Rasouli
mostafarasooli54@gmail.com
August 2024
"""


from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK


def get_response(data=None, errors=None, params=None, status_code=None):
    if errors:
        return Response({
            'Success': False,
            'errors': errors,
            'params': params,
            'data': None
        }, status=status_code or HTTP_400_BAD_REQUEST)

    else:
        return Response({
            'Success': True,
            'errors': None,
            'params': params,
            'data': data
        }, status=status_code or HTTP_200_OK)
