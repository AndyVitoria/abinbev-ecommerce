from fastapi.routing import APIRouter

from src.entities import User
from src.usecases import RegisterUser, UserRole

client_router = APIRouter(tags=["clients"], prefix="/clients")


@client_router.post("/")
def register_client(client_registry: User):
    register_client_use_case = RegisterUser(user=client_registry, role=UserRole.CLIENT)

    register_client_use_case.register_user(client_registry)
    return {"message": "User registered successfully"}
