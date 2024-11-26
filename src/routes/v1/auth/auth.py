from typing import Annotated

from fastapi import Depends, APIRouter, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from src.entities import User
from src.usecases.login import LoginUseCase

auth_router = APIRouter(tags=["auth"], prefix="/auth")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@auth_router.post("/token")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user = User(
        username=form_data.username, password=form_data.password, email="faker@mail.com"
    )
    try:
        login_usecase = LoginUseCase(user=user)
        access_token = login_usecase.generate_token()
    except ValueError as e:
        raise HTTPException(
            status_code=400, detail=str(e), headers={"WWW-Authenticate": "Bearer"}
        )
    except Exception as e:
        # Log the exception to the monitoring service
        raise HTTPException(
            status_code=500,
            detail="Internal server error",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return access_token
