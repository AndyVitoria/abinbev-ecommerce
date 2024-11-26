from typing import Any


class FakerVault:
    """Class for simulate a vault for this project, in real world, this should be a vault service as Azure Key Vault, AWS Secrets Manager, etc."""

    def __init__(self):
        self.__secrets = {
            "SECRET_KEY": "72eaab875e11272400ddfc92f1f84c0cf934bd82a4e3fcb1c3246505f05f1ab1",  # TODO: Store this in a safe place like a Key Vault
            "ALGORITHM": "HS256",  # TODO: Store this in a safe place like a Key Vault
            "ACCESS_TOKEN_EXPIRE_MINUTES": 30,
        }

    def get_secret(self, secret_name: str) -> Any:
        """Get the secret value from the vault

        Parameters
        ----------
        secret_name: str
            The name of the secret to be retrieved

        Returns
        -------
        str
            The secret value

        Raises
        ------
        KeyError
            If the secret name is not found in the vault
        """
        return self.__secrets[secret_name]
