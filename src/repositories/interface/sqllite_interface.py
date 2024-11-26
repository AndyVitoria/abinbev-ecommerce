from typing import Type
from sqlmodel import Session, SQLModel, select
from sqlmodel.sql.expression import BinaryExpression
from src.repositories.database import SQLLiteDatabaseMonostate


class SQLLiteInterface:
    """Interface to interact with the SQLite database"""
    def __init__(self, database_url: str = "sqlite:///./test.db"):
        """Class constructor

        Parameters
        ----------
        database_url: str
            The URL to the SQLite database
        """
        self.database = SQLLiteDatabaseMonostate(database_url)

    def create_or_update(self, model: SQLModel):
        """Creates or updates a model in the database

        Parameters
        ----------
        model: SQLModel
            The model to be created or updated

        Returns
        -------
        SQLModel
            The model created or updated
        """
        with Session(self.database.get_engine()) as session:
            session.add(model)
            session.commit()
        return model

    def list(self, model_class: Type[SQLModel]):
        """Lists all models of a given class

        Parameters
        ----------
        model_class: Type[SQLModel]
            The class of the model to be listed

        Returns
        -------
        List[SQLModel]
            A list of all models of the given class
        """
        with Session(self.database.get_engine()) as session:
            statement = select(model_class)
            return session.exec(statement).all()

    def where(self, model_class: Type[SQLModel], condition: BinaryExpression):
        """Lists all models of a given class that satisfy a given condition

        Parameters
        ----------
        model_class: Type[SQLModel]
            The class of the model to be listed
        condition: BinaryExpression
            The condition to be satisfied by the models

        Returns
        -------
        List[SQLModel]
            A list of all models of the given class that satisfy the given condition
        """
        with Session(self.database.get_engine()) as session:
            statement = select(model_class).where(condition)
            return session.exec(statement).all()
