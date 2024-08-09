"""
common utility functions
Mostafa Rasouli
mostafarasooli54@gmail.com
August 2024
"""


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def get_client_device(request):
    device = request.headers.get("User-Agent")

    return device
