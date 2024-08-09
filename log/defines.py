"""
Log defines
Mostafa Rasouli
mostafarasooli54@gmail.com
August 2024
"""

# Local
from log.models import Log
from utils.functions import get_client_ip, get_client_device


def save_log(request, log_type=None, api=None, log_desc=None):
    try:
        Log.objects.create(
            log_type=log_type,
            api=api,
            request=request.build_absolute_uri(),
            body=request.data,
            user=request.user if request.user.is_authenticated else None,
            log_desc=log_desc,
            ip=get_client_ip(request),
            device=get_client_device(request),
        )
    except Exception:
        pass
