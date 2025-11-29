# --- base_exceptions.py ---
from rest_framework.exceptions import APIException

class DomainException(APIException):
    status_code = 400
    default_detail = 'Domain validation error.'
    default_code = 'domain_error'