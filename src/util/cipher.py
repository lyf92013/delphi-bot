from cryptography.fernet import Fernet
from src.schema import API


class Cipher:
    def __init__(self, key):
        self.key = key
        self.fernet = Fernet(self.key)

    def encrypt(self, api_key: str, api_secret: str):
        text = f"{api_key}/{api_secret}"
        encrypted_text = self.fernet.encrypt(bytes(text, encoding="utf-8"))
        return encrypted_text.decode("utf-8")

    def decrypt(self, encrypted_text) -> API:
        encrypted_bytes = bytes(encrypted_text, encoding="utf-8")
        decrypted_bytes = self.fernet.decrypt(encrypted_bytes)
        api_key, api_secret = decrypted_bytes.decode("utf-8").split("/")
        return API(key=api_key, secret=api_secret)
