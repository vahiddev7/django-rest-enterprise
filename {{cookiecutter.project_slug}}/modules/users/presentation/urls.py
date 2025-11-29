from django.urls import path, include

urlpatterns = [
    path("v1/", include("modules.users.presentation.api.v1.urls"))
]
