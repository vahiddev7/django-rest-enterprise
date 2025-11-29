from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework.authentication import BasicAuthentication
from core.authentication.jwt_auth import JWTAuthentication

class ApiAuthMixin:
    authentication_classes = [JWTAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
