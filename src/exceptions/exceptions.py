from fastapi.exceptions import HTTPException


class CustomHTTPException(HTTPException):
    def __init__(self, status_code: int, detail: str):
        super().__init__(status_code=status_code, detail=detail)
        self.status_code = status_code
        self.detail = detail

    def __str__(self):
        return super().__str__()


class FieldAlreadyInUseError(CustomHTTPException):
    status_code = 400

    def __init__(self, field: str):
        self.field = field
        self.detail = f"{field} already in use"


class AuthenticationError(CustomHTTPException):
    status_code = 401

    def __init__(self, message: str):
        self.detail = f"Authentication failed: {message}"


class ForbiddenError(CustomHTTPException):
    status_code = 403

    def __init__(self):
        self.detail = "Unauthorized"


class NotFoundError(CustomHTTPException):
    status_code = 404

    def __init__(self, entity: str):
        self.detail = f"{entity} not found"


class EntityAlreadyExistsError(CustomHTTPException):
    status_code = 409

    def __init__(self, entity: str):
        self.detail = f"{entity} already exists"


class NotEnoughStockError(CustomHTTPException):
    status_code = 409

    def __init__(self, product: str):
        self.detail = f"Not enough stock for product {product}"
