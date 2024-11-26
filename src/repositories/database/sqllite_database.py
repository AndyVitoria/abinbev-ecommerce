from sqlmodel import create_engine
from sqlalchemy import Engine


class SQLLiteDatabaseMonostate:
    """Class that creates a Monostate instance of a SQLLite database engine"""
    __shared_state = {"engine": None}

    def __new__(cls, database_url, *args, **kwargs):
        obj = super().__new__(cls)
        obj.__dict__ = cls.__shared_state
        if obj.engine is None:
            obj.engine = create_engine(database_url)
        return obj

    def get_engine(self) -> Engine:
        """Returns the engine instance

        Returns
        -------
        Engine
            The engine instance
        """
        return self.engine
