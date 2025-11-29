# --- urls.py ---
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('modules.users.presentation.urls')),
    path('api/auth/', include('modules.authentication.presentation.urls')),
    
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]