class UserPatterns:
    __USERNAME_PATTERN: str = r"^[a-zA-Z][a-zA-Z0-9]{3,19}$"
    __PASSWORD_PATTERN: str = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[\W_]).{8,}$"

    @property
    def USERNAME_PATTERN(self) -> str:
        return self.__USERNAME_PATTERN

    @property
    def PASSWORD_PATTERN(self) -> str:
        return self.__PASSWORD_PATTERN
