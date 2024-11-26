from fastapi.routing import APIRouter, HTTPException

from src.entities import User
from src.usecases import RegisterUser, UserRole


client_router = APIRouter(tags=["clients"], prefix="/clients")


@client_router.post("/")
def register_client(client_registry: User):
    try:
        register_client_usecase = RegisterUser(
            user=client_registry, role=UserRole.CLIENT
        )

        register_client_usecase.register_user(client_registry)

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return {"message": "User registered successfully"}
