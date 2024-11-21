from abc import ABC
from hashlib import sha256
from datetime import datetime
import re
    
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
    __username: str = None
    __password: str = None
    __created_on: datetime = None
    __email: str = None
    __USERNAME_PATTERN: str = r"^[a-zA-Z][a-zA-Z0-9]{3,19}$"
    __PASSWORD_PATTERN: str = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[\W_]).{8,}$"


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
        self.username = username
        self.__set_password(password)
        self.__created_on = datetime.now()
        self.__email = email
    
    def __set_password(self, password: str):
        """Hash and then sets the password for the user.

        Parameters
        ----------
        password : str
            The password to be set.
        """
        if self.__password is not None: #TODO: Add the possibility to change the password
            raise ValueError("Password cannot be changed")
        elif not isinstance(password, str):
            raise TypeError("Password must be a string")
        if re.match(self.__PASSWORD_PATTERN, password) and self.username not in password:
            self.__password = sha256(password.encode()).hexdigest()
        else:
            raise ValueError("Password must have at least 8 characters, one uppercase letter, one lowercase letter, one number, one special character and cannot contain the username on it.")

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
        TypeError
            When the username is not a string
        """
        if self.__username is not None:
            raise ValueError("Username cannot be changed")
        elif not isinstance(username, str):
            raise TypeError("Username must be a string")
        elif re.match(self.__USERNAME_PATTERN, username) is None:
            raise ValueError("Username must be a alphanumeric string between 4 and 20 characters long and start with a letter")
        #TODO: Check if username is already in use
        else:
            self.__username = username
        
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