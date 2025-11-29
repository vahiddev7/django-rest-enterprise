# --- views.py ---
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from modules.authentication.application.usecases import LoginUser
from modules.authentication.infrastructure.serializers import LoginSerializer

class LoginAPIView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        usecase = LoginUser(**serializer.validated_data)
        result = usecase.execute()
        return Response(result, status=status.HTTP_200_OK)