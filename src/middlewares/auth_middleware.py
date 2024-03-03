from fastapi import Request, HTTPException
from jwt import decode
from os import environ, path
from ..models.PayloadModel import PayloadModel
from ..database.db import Database

if path.exists(path.join(path.dirname(__file__), "..", "..", ".env")):
    from dotenv import load_dotenv
    load_dotenv(path.join(path.dirname(__file__), "..", "..", ".env"))



def auth_middleware(request: Request) -> PayloadModel:
    token: str | None = request.headers.get("Authorization")
    if token is None:
        raise HTTPException(status_code=401, detail="Unauthorized")
    token = token.split(" ")[1]
    if token is None:
        raise HTTPException(status_code=401, detail="Unauthorized")
    payload = None
    try:
        payload = decode(token, environ.get("secret_jwt_key"), algorithms=["HS256"])
    except Exception as e:
        raise HTTPException(status_code=401, detail=e.args[0])
    if not Database.fetchOne("id", "users", f"id = {payload['id']}"):
        raise HTTPException(status_code=401, detail="User does not exist")
    return payload
