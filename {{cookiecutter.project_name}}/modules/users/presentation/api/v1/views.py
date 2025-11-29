# --- views.py ---
from rest_framework import generics, permissions
from modules.users.infrastructure.models import User
from modules.users.infrastructure.serializers import UserSerializer

class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = User.objects.using('default').all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class UserRetrieveAPIView(generics.RetrieveAPIView):
    queryset = User.objects.using('default').all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
