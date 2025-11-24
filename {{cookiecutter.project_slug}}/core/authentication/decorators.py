from functools import wraps
from rest_framework.response import Response
from rest_framework import status

def jwt_required(view_func):
    @wraps(view_func)
    def _wrapped_view(self, request, *args, **kwargs):
        if not getattr(request, 'user', None) or not request.user.is_authenticated:
            return Response({"detail": "JWT token required or invalid"}, status=status.HTTP_401_UNAUTHORIZED)
        return view_func(self, request, *args, **kwargs)
    return _wrapped_view
