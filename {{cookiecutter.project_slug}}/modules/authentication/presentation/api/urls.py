# --- urls.py ---
from django.urls import path, include

urlpatterns = [
    path('v1/', include('modules.authentication.presentation.api.v1.urls'))
]