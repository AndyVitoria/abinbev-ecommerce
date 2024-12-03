# routes.py
from fastapi import APIRouter, Depends, HTTPException
from typing import List
from jwt.exceptions import DecodeError
from src.entities import Product, Token
from src.usecases import (
    RegisterProductUseCase,
    LoginUseCase,
)
from src.exceptions import (
    ForbiddenError,
    AuthenticationError,
    EntityAlreadyExistsError,
    NotFoundError,
)


def check_user_authorization(token: Token, product: Product):
    user = LoginUseCase.decode_token_to_user(token.access_token)
    if not user.is_superuser:
        raise ForbiddenError()
    if product.owner_id is not None:
        if product.owner_id != user.id:
            raise AuthenticationError("User is not the owner of the product")
    product.owner_id = user.id


product_router = APIRouter(tags=["products"], prefix="/products")


@product_router.post("/")
def create_product(product: Product, token: Token):
    check_user_authorization(token, product)
    product_use_case = RegisterProductUseCase(product)
    if product_use_case.product_exists(product_name=product.name, product_id=product.id):
        raise EntityAlreadyExistsError("Product")
    else:
        product_use_case.create_or_update_product()
        new_product = product_use_case.product
    return {
        "message": "Product registered successfully",
        "product": {
            "id": new_product.id,
            "name": new_product.name,
            "description": new_product.description,
        },
    }


@product_router.put("/{product_id}")
def update_product(product_id: int, product: Product, token: Token):

    old_product = RegisterProductUseCase.get_product(product_id).to_entity()

    if not old_product:
        raise NotFoundError("Product")
    check_user_authorization(token, old_product)
    product.id = product_id
    product.owner_id = old_product.owner_id
    product_use_case = RegisterProductUseCase(product)
    product_use_case.create_or_update_product()
    new_product = product_use_case.product

    return {
        "message": "Product updated successfully",
        "product": {
            "id": new_product.id,
            "name": new_product.name,
            "description": new_product.description,
        },
    }


@product_router.delete("/{product_id}")
def delete_product(product_id: int, token: Token):
    product = RegisterProductUseCase.get_product(product_id).to_entity()
    if not product:
        raise NotFoundError("Product")

    check_user_authorization(token, product)
    product.is_active = False
    product_use_case = RegisterProductUseCase(product)
    product_use_case.create_or_update_product()
    new_product = product_use_case.product  
    return {
        "detail": "Product deleted",
        "product": {
            "id": new_product.id,
            "name": new_product.name,
            "description": new_product.description,
        },
    }


@product_router.get("/{product_id}")
def get_product(product_id: int, token: Token):
    product = RegisterProductUseCase.get_product(product_id).to_entity()
    if not product:
        raise NotFoundError("Product")
    return {
        "product": {
            "id": product.id,
            "name": product.name,
            "description": product.description,
            "price": product.price,
            "stock": product.stock,
            "is_active": product.is_active,
        }
    }

@product_router.get("/")
def list_products():
    products:List[Product] = RegisterProductUseCase.list_products()
    return {
        "products": [
            {
                "id": product.id,
                "name": product.name,
                "description": product.description,
                "price": product.price,
                "price": product.price,
                "stock": product.stock,
                "is_active": product.is_active,
            }
            for product in products
        ]
    }