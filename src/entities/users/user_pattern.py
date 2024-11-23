class UserPatterns:
    __USERNAME_PATTERN: str = r"^[a-zA-Z][a-zA-Z0-9]{3,19}$"
    __PASSWORD_PATTERN: str = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[\W_]).{8,}$"

    @property
    def USERNAME_PATTERN(cls) -> str:
        return cls.__USERNAME_PATTERN
    
    @property
    def PASSWORD_PATTERN(cls) -> str:
        return cls.__PASSWORD_PATTERN