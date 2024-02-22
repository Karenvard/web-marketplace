'''
Author: Karen Vardanian (vkaren1777@icloud.com)
File Created: Thursday, 22nd February 2024 8:59:04 pm
Copyright © 2024 - Karen Vardanian
'''


from bcrypt import hashpw, gensalt, checkpw
from typing import Dict
from os import environ
from jwt import encode
from models.signup_model import SignupModel

class UserHandler:
    def _generateJwtToken(self, payload: Dict[str, str]) -> str:
        return encode(payload, environ.get("secret_jwt_key"), algorithm="HS256")

    def signup(self, body: SignupModel) -> None:
        pass

    def signin(self) -> None:
        pass