from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

health_router = APIRouter()


@health_router.get("/health", tags=["health"])
def read_health(request: Request) -> dict:
    return JSONResponse(status_code=200, content={"status": "ok"})
