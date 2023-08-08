from dependency_injector import containers, providers
from src.util.cipher import Cipher
from src.util.setting import Settings


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()
    config.from_pydantic(Settings())

    cipher = providers.Singleton(
        Cipher,
        key=config.cipher_key,
    )
