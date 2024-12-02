from sqlmodel import SQLModel, Field

from src.entities.products import Product
from .user_model import UserModel


class ProductModel(SQLModel, table=True):
    """ProductModel is a SQLModel representation of the Product entity"""

    id: int = Field(primary_key=True)
    name: str
    description: str
    price: float
    stock: int
    owner_id: int = Field(default=None, foreign_key="usermodel.id")
    is_active: bool = Field(default=True)

    @classmethod
    def from_entity(cls, entity: Product):
        """Creates an instance of ProductModel based on the Product entity provided

        Parameters
        ----------
        entity: Product
            The product entity to be converted to a ProductModel

        Returns
        -------
        ProductModel
            The ProductModel created based on the Product entity provided
        """
        return cls(
            id=entity.id,
            name=entity.name,
            description=entity.description,
            price=entity.price,
            stock=entity.stock,
            owner_id=entity.owner_id,
            is_active=entity.is_active,
        )

    def to_entity(self):
        """Creates an instance of Product based on the ProductModel provided

        Returns
        -------
        Product
            The Product created based on the ProductModel provided
        """
        return Product(
            id=self.id,
            name=self.name,
            description=self.description,
            price=self.price,
            stock=self.stock,
            owner_id=self.owner_id,
            is_active=self.is_active,
        )
