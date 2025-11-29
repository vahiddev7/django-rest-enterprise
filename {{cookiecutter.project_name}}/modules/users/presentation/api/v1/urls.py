# --- urls.py ---
from django.urls import path
from .views import UserListCreateAPIView, UserRetrieveAPIView

urlpatterns = [
    path('', UserListCreateAPIView.as_view(), name='user-list'),
    path('<int:pk>/', UserRetrieveAPIView.as_view(), name='user-detail'),
]