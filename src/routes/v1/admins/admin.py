from fastapi.routing import APIRouter, HTTPException

from src.entities import User
from src.usecases import RegisterUser, UserRole


admin_router = APIRouter(tags=["admins"], prefix="/admins")


@admin_router.post("/")
def register_admin(client_registry: User):
    # TODO: Add authentication to this endpoint to ensure only admins can register new admins
    register_client_use_case = RegisterUser(user=client_registry, role=UserRole.ADMIN)

    register_client_use_case.register_user(client_registry)
    return {"message": "User registered successfully"}
