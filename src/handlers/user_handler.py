'''
Author: Karen Vardanian (vkaren1777@icloud.com)
File Created: Sunday, 25th February 2024 11:41:33 am
Copyright © 2024 - Karen Vardanian
'''


from bcrypt import hashpw, gensalt, checkpw
from datetime import datetime, timedelta
from typing import Dict
from os import environ
from jwt import encode
from models import SignupModel, SigninModel
from fastapi import Depends, HTTPException
from middlewares.auth_middleware import auth_middleware
from models import PayloadModel, UserModel
from database.db import Database

class UserHandler:

    @staticmethod
    def _generateJwtToken(payload: PayloadModel, remember_me: bool) -> str:
        return encode(payload.model_dump(), environ.get("secret_jwt_key"), algorithm="HS256", headers={"expiration": 24*60*60 if remember_me else 3*60*60})


    @staticmethod
    def signup(signup: SignupModel) -> Dict[str, str]:
        candidate = Database.fetchOne("*", "users", f"email = '{signup.email}'")
        if candidate:
            raise HTTPException(status_code=400, detail="Email already registered.")
        Database.insertInto("users", "fullname, email, password", f"'{signup.fullname}', '{signup.email}', '{hashpw(signup.password.encode('utf-8'), gensalt()).decode('utf-8')}'")
        createdUserId = Database.fetchOne("id", "users", f"email = '{signup.email}'")[0]
        Database.insertInto("baskets", "user_id", f"{createdUserId}")
        createdBasketId = Database.fetchOne("id", "baskets", f"user_id = {createdUserId}")[0]
        Database.update("users", f"basket_id = '{createdBasketId}'", f"id = {createdUserId}")
        return {"message": "User created successfully."}


    @staticmethod
    def signin(signin: SigninModel):
        user = Database.fetchOne("id, email, password, fullname", "users", f"email = '{signin.email}';")
        if not user:
            raise HTTPException(status_code=400, detail="Invalid email or password.")
        if not checkpw(signin.password.encode('utf-8'), user[2].encode('utf-8')):
            raise HTTPException(status_code=400, detail="Invalid email or password.")
        payload = PayloadModel(id=user[0], email=user[1], fullname=user[3])
        token = UserHandler._generateJwtToken(payload, signin.remember_me)
        return {"token": token}
    
    @staticmethod
    def getAuthenticatedUser(payload: PayloadModel.model_dump = Depends(auth_middleware)) -> UserModel:
        user = Database.fetchOne("id, fullname, email, basket_id, seller_id, created", "users", f"id = {payload['id']};")
        return UserModel(id=user[0], fullname=user[1], email=user[2], basket_id=user[3], seller_id=user[4], created=user[5])
        

