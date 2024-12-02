from fastapi import FastAPI
import uvicorn
from fastapi.exceptions import HTTPException, RequestValidationError

from src.routes.health import health_router
from src.routes.v1 import (
    client_router,
    auth_router,
    admin_router,
    product_router,
    cart_router,
    order_router,
)
from src.exceptions.handlers import (
    http_exception_handler,
    validation_exception_handler,
    general_exception_handler,
)


app = FastAPI()

# Include routers
app.include_router(health_router)
app.include_router(client_router, prefix="/v1")
app.include_router(auth_router, prefix="/v1")
app.include_router(product_router, prefix="/v1")
app.include_router(admin_router, prefix="/v1")
app.include_router(cart_router, prefix="/v1")
app.include_router(order_router, prefix="/v1")


# Add exception handlers
app.add_exception_handler(HTTPException, http_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(Exception, general_exception_handler)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
