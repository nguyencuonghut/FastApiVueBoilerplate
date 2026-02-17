class APIException(Exception):
    """Custom API exception"""
    def __init__(self, message: str, status_code: int = 400):
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)


class AuthenticationException(APIException):
    """Authentication failed"""
    def __init__(self, message: str = "Authentication failed"):
        super().__init__(message, status_code=401)


class AuthorizationException(APIException):
    """User not authorized"""
    def __init__(self, message: str = "Access denied"):
        super().__init__(message, status_code=403)


class ResourceNotFoundException(APIException):
    """Resource not found"""
    def __init__(self, message: str = "Resource not found"):
        super().__init__(message, status_code=404)


class ValidationException(APIException):
    """Validation error"""
    def __init__(self, message: str = "Validation failed"):
        super().__init__(message, status_code=422)
