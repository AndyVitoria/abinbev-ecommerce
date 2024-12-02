from pydantic import BaseModel, field_validator
from typing import Optional

from .. import User


class Product(BaseModel):
    id: Optional[int] = None
    name: str
    description: str
    price: float
    stock: int
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    owner_id: Optional[int] = None
    is_active: Optional[bool] = True

    @field_validator("price")
    def validate_price(cls, price: float):
        if price < 0:
            raise ValueError("Price must be greater than 0")
        return price

    @field_validator("stock")
    def validate_stock(cls, stock: int):
        if stock < 0:
            raise ValueError("Stock must be greater than 0")
        return stock

    @field_validator("name")
    def validate_name(cls, name: str):
        if len(name) < 3:
            raise ValueError("Name must be at least 3 characters long")
        return name

    @field_validator("is_active")
    def validate_is_active(cls, is_active: bool = None):
        if is_active or is_active is None:
            return True
        return False
