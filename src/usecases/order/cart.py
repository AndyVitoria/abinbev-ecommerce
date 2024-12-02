from src.entities import CartItem
from src.repositories.models import CartItemModel, ProductModel
from src.repositories.interface import SQLLiteInterface
from src.exceptions import NotFoundError, NotEnoughStockError
from typing import  Optional

class CartUseCase:
    __database_interface = SQLLiteInterface()

    def __init__(self, user_id: int):
        self.__user_id = user_id
        self.__cart_items = self.__get_cart_items()

    def __get_cart_items(self):
        list_items = self.__database_interface.where(
            model_class=CartItemModel,
            condition=(CartItemModel.user_id == self.__user_id),
        )
        return {cart_item.product_id: cart_item for cart_item in list_items}

    def get_cart_items(self):
        return self.__cart_items

    def refresh_cart(self):
        self.__cart_items = self.__get_cart_items()

    def get_item(self, product_id: int) -> Optional[CartItem]:
        return self.__cart_items.get(product_id, None)

    def __get_product(self, product_id: int):
        return self.__database_interface.get_model_by_id(ProductModel, product_id)

    def add_item(self, cart_item: CartItem):
        self.refresh_cart()
        product = self.__get_product(cart_item.product_id)
        if not product:
            raise NotFoundError("Product")

        cart_item_model: CartItemModel = self.get_item(cart_item.product_id)
        current_quantity = 0 if cart_item_model is None else cart_item_model.quantity
        if current_quantity + cart_item.quantity > product.stock:
            raise NotEnoughStockError(f"{(product.id, product.name)}")
        if cart_item_model:
            cart_item_model.quantity += cart_item.quantity

            self.__database_interface.update(cart_item_model)
        else:
            cart_item.user_id = self.__user_id
            cart_item_model = CartItemModel.from_entity(cart_item)

            self.__database_interface.create(cart_item_model)
            self.__cart_items[cart_item.product_id] = cart_item
        self.refresh_cart()
        return self.get_item(cart_item.product_id).to_entity()

    def remove_item(self, product_id: int, quantity: int = None):
        self.refresh_cart()
        cart_item_model = self.get_item(product_id)
        if cart_item_model:
            if quantity is None or quantity >= cart_item_model.quantity:
                self.__database_interface.delete(cart_item_model)
                del self.__cart_items[product_id]
            else:
                cart_item_model.quantity -= quantity
                self.__database_interface.update(cart_item_model)
                self.refresh_cart()
                return self.get_item(product_id).to_entity()
        return None

    def clear_cart(self):
        for cart_item in self.__cart_items.values():
            self.__database_interface.delete(cart_item)
        self.__cart_items.clear()
        return True
