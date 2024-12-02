from src.repositories.models import OrderModel, ProductModel, OrderedItemModel
from src.entities import Order, OrderedItem
from src.repositories.interface import SQLLiteInterface
from src.exceptions import NotEnoughStockError, NotFoundError
from .cart import CartUseCase


class OrderUseCase:
    __database_interface = SQLLiteInterface()

    def __init__(self, user_id: int):
        self.__user_id = user_id
        self.__cart_use_case = CartUseCase(self.__user_id)
        self.__order = self.create_order(self.__user_id)

    def create_order_model(self):
        return OrderModel.from_entity(self.__order)

    def create_order(self, user_id: int):
        cart_items = self.__cart_use_case.get_cart_items().values()
        if not cart_items:
            raise NotFoundError("Cart")
        total_price = 0
        ordered_items = list()
        for cart_item in cart_items:
            product_model = self.__database_interface.get_model_by_id(
                ProductModel, cart_item.product_id
            )
            if product_model is None:
                raise NotFoundError("Product ID: " + str(cart_item.product_id))
            elif (
                product_model.stock < cart_item.quantity or not product_model.is_active
            ):
                raise NotEnoughStockError(
                    f"{product_model.name, product_model.stock, cart_item.quantity}"
                )

            ordered_item = OrderedItem(
                product_id=cart_item.product_id,
                quantity=cart_item.quantity,
                price=product_model.price,
            )
            total_price += ordered_item.total_price
            ordered_items.append(ordered_item)
        return Order(user_id=user_id, items=ordered_items, total_price=total_price)

    def __update_product_stock(self):
        cart_items = self.__cart_use_case.get_cart_items().values()
        for cart_item in cart_items:
            product_model = self.__database_interface.get_model_by_id(
                ProductModel, cart_item.product_id
            )
            product_model.stock -= cart_item.quantity
            self.__database_interface.update(product_model)

    def make_order(self):
        order_model = self.create_order_model()
        self.__database_interface.create(order_model)
        self.__update_product_stock()
        self.__cart_use_case.clear_cart()
        return self.__order

    @classmethod
    def get_order(cls, order_id: int):
        return cls.__database_interface.get_model_by_id(OrderModel, order_id, return_entity=True)

    @classmethod
    def get_orders(cls, user_id: int):
        return cls.__database_interface.where(OrderModel, condition=(OrderModel.user_id == user_id), return_entity=True)
        

    def check_payment(self):
        return True

    @property
    def order(self) -> Order:
        return self.__order
