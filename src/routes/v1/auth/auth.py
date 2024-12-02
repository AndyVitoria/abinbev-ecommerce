from typing import Annotated
from fastapi import Depends, APIRouter, HTTPException, status
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
    login_use_case = LoginUseCase(user=user)
    access_token = login_use_case.generate_token()
    return access_token
