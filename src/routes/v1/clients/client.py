from fastapi.routing import APIRouter, HTTPException

from src.entities import ClientUser

client_router = APIRouter(tags=["clients"], prefix="/clients")

@client_router.post("/")
def register_client(client_registry: ClientUser):
    # Here you would typically add logic to save the user to a database
    # For this example, we'll just print the user data and return a success message

    try:
        print(f"Registering Client: {client_registry.username}, Email: {client_registry.email}")
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return {"message": "User registered successfully"}

