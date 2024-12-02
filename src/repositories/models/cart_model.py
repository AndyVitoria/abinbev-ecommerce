from sqlmodel import SQLModel, Field, Relationship

from src.entities import CartItem
from . import ProductModel


class CartItemModel(SQLModel, table=True):
    """CartItemModel is a SQLModel representation of the CartItem entity"""

    id: int = Field(primary_key=True)
    product_id: int = Field(default=None, foreign_key="productmodel.id")
    quantity: int
    user_id: int = Field(default=None, foreign_key="usermodel.id")

    @classmethod
    def from_entity(cls, entity: CartItem):
        """Creates an instance of CartItemModel based on the CartItem entity provided

        Parameters
        ----------
        entity: CartItem
            The cart item entity to be converted to a CartItemModel

        Returns
        -------
        CartItemModel
            The CartItemModel created based on the CartItem entity provided
        """
        return cls(
            product_id=entity.product_id,
            quantity=entity.quantity,
            user_id=entity.user_id,
        )

    def to_entity(self):
        """Creates an instance of CartItem based on the CartItemModel provided

        Returns
        -------
        CartItem
            The CartItem created based on the CartItemModel provided
        """
        return CartItem(
            product_id=self.product_id,
            quantity=self.quantity,
            user_id=self.user_id,
        )
