from os import getenv
import bcrypt
from jwt import encode
from database.db import Database
from dto.AddUserDto import AddUserDto
from dto.SigninDto import SigninDto
from dto.UpdateUserDto import UpdateUserDto
from models.PayloadModel import PayloadModel
from models.SuccessfulResponse import SuccessfulResponse
from fastapi import Depends, HTTPException
from typing import Any, Dict, Tuple
from middlewares.auth_middleware import auth_middleware
import datetime


class user_handler:

    @staticmethod
    def _generate_jwt_token(payload: PayloadModel) -> str:
        secret_jwt_key: str | None = getenv("secret_jwt_key")
        if not secret_jwt_key:
            raise HTTPException(status_code=500, detail="Internal server error.")
        return encode(dict(payload), secret_jwt_key, algorithm="HS256").decode("utf-8")

    @staticmethod
    def signup(dto: AddUserDto) -> SuccessfulResponse:
        # 1. get candidate
        # 2. check if candidate exists
        # 3. Hash password
        # 4. Insert user into database with hashed password
        # 5. Return success message {"message": "User was created successfully."}
        candidate = Database.fetchOne(
            f"SELECT * FROM USERS WHERE username = '{dto.username}'"
        )
        if candidate:
            raise HTTPException(status_code=400, detail="User already exists.")
        hashedPassword: str = bcrypt.hashpw(
            dto.password.encode("utf-8"), bcrypt.gensalt()
        ).decode("utf-8")
        Database.commit(
            f"INSERT INTO USERS (fullname, username, password) VALUES ('{dto.fullname}', '{dto.username}', '{hashedPassword}')"
        )
        added_user_id = Database.fetchOne(
            f"SELECT id FROM users WHERE username = '{dto.username}'"
        )
        Database.commit(f"INSERT INTO baskets (user_id) VALUES ({added_user_id})")
        Database.commit(
            f"INSERT INTO users (basket_id) VALUES ({added_user_id}) WHERE id = {added_user_id}"
        )
        return {"message": "User was created successfully."}

    @staticmethod
    def signin(dto: SigninDto) -> Dict[str, str]:
        # 1. get user
        # 2. check if user exists
        # 3. check if password is correct
        # 4. return success message {"message": "User was signed in successfully."}
        user = Database.fetchOne(
            f"SELECT id, username, password, role_id FROM USERS WHERE username = '{dto.username}'"
        )
        if not user:
            raise HTTPException(status_code=400, detail="Invalid username or password.")
        if not bcrypt.checkpw(dto.password.encode("utf-8"), user[2].encode("utf-8")):
            raise HTTPException(status_code=400, detail="Invalid username or password.")
        token = user_handler._generate_jwt_token(
            PayloadModel(id=user[0], username=user[1], role_id=user[3])
        )
        return {"token": token}

    @staticmethod
    def get_authenticated(
        payload: PayloadModel = Depends(auth_middleware),
    ) -> Dict[str, Any]:
        # 1. get user
        # 2. return user
        data: Tuple[int, str, str, int, datetime.datetime] = Database.fetchOne(
            f"SELECT id, username, fullname, role_id, created FROM USERS WHERE id = {payload['id']}"
        )
        user = {
            "id": data[0],
            "username": data[1],
            "fullname": data[2],
            "role_id": data[3],
            "created": data[4],
        }
        return user

    @staticmethod
    def update(
        dto: UpdateUserDto, payload: PayloadModel = Depends(auth_middleware)
    ) -> SuccessfulResponse:
        # 1. get user
        # 2. update user
        user_password = Database.fetchOne(
            f"SELECT password FROM USERS WHERE id = {payload['id']}"
        )[0]
        if not bcrypt.checkpw(
            dto.verify_password.encode("utf-8"), user_password.encode("utf-8")
        ):
            raise HTTPException(status_code=400, detail="Invalid password.")
        if dto.fullname is None and dto.username is None and dto.password is None:
            raise HTTPException(status_code=400, detail="Nothing to update.")
        if dto.fullname is not None:
            Database.commit(
                f"UPDATE users SET fullname = '{dto.fullname}' WHERE id = {payload['id']}"
            )
        if dto.username is not None:
            Database.commit(
                f"UPDATE users SET username = '{dto.username}' WHERE id = {payload['id']}"
            )
        if dto.password is not None:
            hashedPassword: str = bcrypt.hashpw(
                dto.password.encode("utf-8"), bcrypt.gensalt()
            ).decode("utf-8")
            Database.commit(
                f"UPDATE users SET password = '{hashedPassword}' WHERE id = {payload['id']}"
            )
        return {"message": "User was updated successfully."}

    @staticmethod
    def get(
        user_id: int, payload: PayloadModel = Depends(auth_middleware)
    ) -> Dict[str, str]:
        """GET USER FROM DATABASE (PATH_PARAMS=user_id)"""
        data = Database.fetchOne(
            f"SELECT id, username, fullname, role_id, created FROM USERS WHERE id = {user_id}"
        )
        user = {
            "id": data[0],
            "username": data[1],
            "fullname": data[2],
            "role_id": data[3],
            "created": data[4],
        }
        return user

    @staticmethod
    def delete(payload: PayloadModel = Depends(auth_middleware)) -> SuccessfulResponse:
        # 1. get user
        # 2. delete user
        Database.commit(f"DELETE FROM users WHERE id = {payload['id']}")
        return {"message": "User was deleted successfully."}
