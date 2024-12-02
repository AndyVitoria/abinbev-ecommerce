from sqlmodel import create_engine, SQLModel

from src.repositories.models import (
    UserModel,
    ProductModel,
    CartItemModel,
    OrderModel,
    OrderedItemModel,
)

connection_str = "sqlite:///./test.db"  # Turn into an environment variable

engine = create_engine(connection_str)

UserModel.metadata.create_all(engine)
ProductModel.metadata.create_all(engine)
CartItemModel.metadata.create_all(engine)
OrderModel.metadata.create_all(engine)
OrderedItemModel.metadata.create_all(engine)
