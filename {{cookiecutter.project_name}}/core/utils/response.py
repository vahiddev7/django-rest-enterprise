# --- response.py ---
from rest_framework.response import Response

def success(data=None, message="Success", status=200):
    return Response({"status": True, "message": message, "data": data}, status=status)

def error(message="Error", status=400, data=None):
    return Response({"status": False, "message": message, "data": data}, status=status)