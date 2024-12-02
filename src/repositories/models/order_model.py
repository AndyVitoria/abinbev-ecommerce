from sqlmodel import SQLModel, Field, Relationship
from typing import List, Optional

from src.entities import Order, OrderedItem


class OrderedItemModel(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    order_id: int = Field(foreign_key="ordermodel.id")
    product_id: int
    quantity: int
    price: float
    order: Optional["OrderModel"] = Relationship(back_populates="items")

    @property
    def total_price(self):
        return self.price * self.quantity

    @classmethod
    def from_entity(cls, item: OrderedItem):
        return cls(product_id=item.product_id, quantity=item.quantity, price=item.price)

    def to_entity(self):
        return OrderedItem(
            product_id=self.product_id, quantity=self.quantity, price=self.price
        )


class OrderModel(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    user_id: int
    total_price: float
    items: List[OrderedItemModel] = Relationship(back_populates="order")

    @classmethod
    def from_entity(cls, order: Order):
        return cls(
            user_id=order.user_id,
            total_price=order.total_price,
            items=[OrderedItemModel.from_entity(item) for item in order.items],
        )

    def to_entity(self):
        return Order(
            id=self.id,
            user_id=self.user_id,
            total_price=self.total_price,
            items=[item.to_entity() for item in self.items],
        )
