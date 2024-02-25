from fastapi import FastAPI, Request, HTTPException
from jwt import decode
from os import environ, path
from models import PayloadModel

if path.exists(path.join(path.dirname(__file__), "..", "..", ".env")):
    from dotenv import load_dotenv
    load_dotenv(path.join(path.dirname(__file__), "..", "..", ".env"))

app = FastAPI()


def auth_middleware(request: Request) -> PayloadModel:
    token: str = request.headers.get("Authorization").split(" ")[1]
    if token is None:
        raise HTTPException(status_code=401, detail="Unauthorized")
    payload = None
    try:
        payload = decode(token, environ.get("secret_jwt_key"), algorithms=["HS256"])
    except Exception as e:
        raise HTTPException(status_code=401, detail=e.args[0])
    return payload
