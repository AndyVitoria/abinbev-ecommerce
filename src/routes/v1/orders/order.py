# routes.py
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from src.entities import Order, Token
from src.usecases import LoginUseCase, OrderUseCase
from src.utils.logger import Logger

from src.exceptions import NotFoundError, AuthenticationError

order_router = APIRouter(tags=["orders"], prefix="/orders")

logger = Logger(name="order_router").get_logger()


@order_router.post("/")
def create_new_order(token: Token):
    user = LoginUseCase.decode_token_to_user(token.access_token)
    logger.debug(f"User: {user}")
    order_use_case = OrderUseCase(user_id=user.id)
    logger.debug(f"Order Use Case: {order_use_case}")
    if order_use_case.check_payment():  # Always returns True
        order = order_use_case.make_order()
    else:
        raise HTTPException(status_code=400, detail="Payment failed")
    return {"message": "Order created successfully", "order_details": order}


@order_router.get("/{order_id}")
def get_order(order_id: int, token: Token):
    user = LoginUseCase.decode_token_to_user(token.access_token)
    order = OrderUseCase.get_order(order_id=order_id)
    if order is None:
        raise NotFoundError("Order")
    if order.user_id == user.id:
        return order
    else:
        raise AuthenticationError("User is not authorized to view this order")
