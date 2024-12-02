from src.repositories.models import ProductModel
from src.entities import Product
from src.repositories.interface import SQLLiteInterface
from src.exceptions import AuthenticationError


class RegisterProductUseCase:
    __database_interface = SQLLiteInterface()

    def __init__(self, product: Product):
        self.__product = product

    def create_model(self):
        return ProductModel.from_entity(self.__product)

    def create_or_update_product(self):
        product_model = self.create_model()
        if self.__product.id is None:
            return self.__create(product_model)
        else:
            old_product_model = self.get_product(self.__product.id)
            return self.__update(product_model, old_product_model)

    def __create(self, product_model):
        return self.__database_interface.create(product_model)

    def __update(self, new_product_model, old_product_model):
        if new_product_model.owner_id != old_product_model.owner_id:
            raise AuthenticationError("Only the owner can update the product")
        return self.__database_interface.update(new_product_model)

    @classmethod
    def product_exists(cls, product_id: int = None, product_name: str = None):
        return (
            len(
                cls.__database_interface.where(
                    ProductModel,
                    condition=(
                        (ProductModel.id == product_id)
                        | (ProductModel.name == product_name)
                    ),
                )
            )
            > 0
        )

    @classmethod
    def get_product(cls, product_id):
        database_interface = SQLLiteInterface()
        return database_interface.get_model_by_id(ProductModel, product_id)

    def deactivate_product(self):
        self.__product.is_active = False
        self.__database_interface.create_or_update_product()
        return self.__product
