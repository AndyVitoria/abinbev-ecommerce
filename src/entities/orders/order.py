from pydantic import BaseModel, field_validator, Field
from typing import List, Optional

from . import CartItem


class OrderedItem(BaseModel):
    product_id: int
    quantity: int
    price: float

    @property
    def total_price(self):
        return self.price * self.quantity


class Order(BaseModel):
    id: Optional[int] = Field(default=None)
    user_id: int
    items: List[OrderedItem]
    total_price: Optional[float]

    def model_post_init(self, __context):
        self.total_price = sum([item.total_price for item in self.items])
        return super().model_post_init(__context)

    @field_validator("items")
    def validate_items(cls, items):
        if not items:
            raise ValueError("Order must have at least one item")

        return items
