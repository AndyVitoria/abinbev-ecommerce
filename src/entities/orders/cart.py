from pydantic import BaseModel, Field, field_validator


class CartItem(BaseModel):
    product_id: int
    quantity: int
    user_id: int = None

    @field_validator("product_id")
    def validate_product_id(cls, product_id: int):
        if product_id < 0:
            raise ValueError("Product ID must be greater than 0")
        return product_id

    @field_validator("quantity")
    def validate_quantity(cls, quantity: int):
        if quantity < 0:
            raise ValueError("Quantity must be greater than 0")
        return quantity

    @field_validator("user_id")
    def validate_user_id(cls, user_id: int):
        if user_id < 0:
            raise ValueError("User ID must be greater than 0")
        return user_id
