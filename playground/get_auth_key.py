import os
import sys

# in order to import python module correctly
sys.path.insert(0, os.getcwd())

from src.container import Container

container = Container()
cipher = container.cipher()
auth_key = cipher.encrypt(
    api_key="07f697a3bf72462ef7ed967856c1e92490c04550e0474ce306153a5300ca6392",
    api_secret="4242659f8ff25affda3e73d312b5ce04c00bb0dd508edda9f468bab3940116de",
)
print(auth_key)
