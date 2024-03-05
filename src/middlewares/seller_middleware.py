from fastapi import Request, HTTPException
from os import path
from models.PayloadModel import PayloadModel
from models.SellerPayloadModel import SellerPayloadModel
from .auth_middleware import auth_middleware
from database.db import Database

if path.exists(path.join(path.dirname(__file__), "..", "..", ".env")):
    from dotenv import load_dotenv
    load_dotenv(path.join(path.dirname(__file__), "..", "..", ".env"))


def seller_middleware(request: Request) -> SellerPayloadModel:
    payload: PayloadModel = auth_middleware(request)
    seller_id = Database.fetchOne(f"SELECT seller_id FROM users WHERE id = {payload['id']}")[0]
    if not seller_id:
        raise HTTPException(status_code=400, detail="You are not a seller.")
    sellerPayload: SellerPayloadModel = {
        "id": payload['id'],
        "username": payload['username'],
        "seller_id": seller_id,
        "role_id": payload['role_id']
    }
    return sellerPayload
