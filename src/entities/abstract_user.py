from abc import ABC
from hashlib import sha256
from datetime import datetime
    
class AbstractUser(ABC):
    """The AbstractUser class is an abstract class that defines the basic structure of a user.

    Attributes
    ----------
        username: str
            The user's username.
        created_on: datetime
            The date and time when the user was created.
        email: str
            The user's e-mail.

    Raises
    ------
    ValueError
        When trying to change inmutable attributes such as username, created_on, or email properties.
    """
    __username: str
    __password: str
    __created_on: datetime
    __email: str

    def __init__(self, username: str, password: str, email: str):
        """Class Constructor

        Parameters
        ----------
        username: str
            The user's username.
        password: str
            The user's password.
        email: str
            The user's email.
        """
        self.__username = username
        self.__password = self.__set_password(password)
        self.__created_on = datetime.now()
        self.__email = email
    
    def __set_password(self, password: str):
        """Hash and then sets the password for the user.

        Parameters
        ----------
        password : str
            The password to be set.
        """
        self.__password = sha256(password.encode()).hexdigest()

    def validate_user():
        """Validates the user's information."""
        return True
    
    @property
    def username(self):
        """Property for the username attribute.

        Returns
        -------
        str
            The username of the user.
        """
        return self.__username
    
    @username.setter
    def username(self, username: str):
        """Property for seting the username attribute.

        Parameters
        ----------
        username : str
            The username to be set.

        Raises
        ------
        ValueError
            When trying to change the username already set.
        """
        raise ValueError("Username cannot be changed")
    
    @property
    def created_on(self):
        """Property for the created_on attribute.

        Returns
        -------
        datetime
            The datetime when the user was created.
        """
        return self.__created_on
    
    @created_on.setter
    def created_on(self, created_on: datetime):
        """Property for setting the created_on attribute.

        Parameters
        ----------
        created_on : datetime
            The datetime to be set.

        Raises
        ------
        ValueError
            When trying to change the created_on attribute already set.
        """
        raise ValueError("Creation date cannot be changed")
    
    @property
    def email(self):
        """Property for the email attribute.

        Returns
        -------
        str
            The email of the user.
        """
        return self.__email
    
    @email.setter
    def email(self, email):
        """_summary_

        Parameters
        ----------
        email : str
            The user's e-mail to be set.

        Raises
        ------
        ValueError
            When trying to change the email attribute already set.
        """
        raise ValueError("Email cannot be changed")
    
    def authenticate(self, password: str):
        """Provisory method to authenticates the user with the given password.

        Parameters
        ----------
        password : str
            The password to be used for authentication

        Returns
        -------
        bool
            True if the password matches the user's password, False otherwise.
        """
        return self.__password == sha256(password.encode()).hexdigest()