from fastapi.routing import APIRouter, HTTPException
from typing import Union
from src.entities import CartItem, Token, Product
from src.usecases import CartUseCase, LoginUseCase
from src.exceptions import ForbiddenError, AuthenticationError

cart_router = APIRouter(tags=["cart"], prefix="/orders/cart")


@cart_router.put("/item")
def add_item(cart_item: CartItem, token: Token):
    user = LoginUseCase.decode_token_to_user(token.access_token)
    if user.id != cart_item.user_id:
        raise AuthenticationError("The user is not authorized to perform this action")

    cart_use_case = CartUseCase(cart_item.user_id)
    return cart_use_case.add_item(cart_item)


@cart_router.delete("/item")
def remove_item(cart_item: CartItem, token: Token):
    user = LoginUseCase.decode_token_to_user(token.access_token)
    if user.id != cart_item.user_id:
        raise AuthenticationError("The user is not authorized to perform this action")

    cart_use_case = CartUseCase(cart_item.user_id)
    response = cart_use_case.remove_item(cart_item.product_id, cart_item.quantity)
    response = response if response else {**cart_item.model_dump(), "quantity": 0}
    return response


@cart_router.get("/items")
def get_cart_items(token: Token):
    user = LoginUseCase.decode_token_to_user(token.access_token)
    cart_use_case = CartUseCase(user.id)
    return [ cart_item.to_entity() for cart_item in
        cart_use_case.get_cart_items().values()
    ]


@cart_router.delete("/items")
def clear_cart_items(token: Token):
    user = LoginUseCase.decode_token_to_user(token.access_token)
    cart_use_case = CartUseCase(user.id)
    cart_use_case.clear_cart()
    return {"message": "cart cleared"}
