import jwt

from passlib.context import CryptContext
from typing import Union
from datetime import timedelta, datetime, timezone


class CryptUtils:
    def __init__(self, SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES: int = 30):
        self.__SECRET_KEY = SECRET_KEY
        self.__ALGORITHM = ALGORITHM
        self.__ACCESS_TOKEN_EXPIRE_MINUTES = ACCESS_TOKEN_EXPIRE_MINUTES
        self.__pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def verify_password(self, plain_password: str, hashed_password: str):
        return self.__pwd_context.verify(plain_password, hashed_password)

    def hash_password(self, password: str):
        return self.__pwd_context.hash(password)

    def create_access_token(self, data: dict):
        to_encode = data.copy()
        expires_delta = timedelta(self.__ACCESS_TOKEN_EXPIRE_MINUTES)
        if expires_delta:
            expiration = datetime.now(timezone.utc) + expires_delta
        else:
            expiration = datetime.now(timezone.utc) + timedelta(minutes=15)
        to_encode.update({"expiration": expiration.isoformat()})
        encoded_jwt = jwt.encode(
            to_encode, self.__SECRET_KEY, algorithm=self.__ALGORITHM
        )
        return encoded_jwt

    def decode_access_token(self, token: str):
        return jwt.decode(token, self.__SECRET_KEY, algorithms=[self.__ALGORITHM])

    def is_token_expired(self, token: str):
        decoded_token = self.decode_access_token(token)
        expiration = datetime.fromisoformat(decoded_token["expiration"])
        return expiration < datetime.now(timezone.utc)
