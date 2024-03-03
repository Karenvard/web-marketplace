from fastapi import Request, HTTPException
from os import path
from ..models.SellerPayloadModel import SellerPayloadModel
from .seller_middleware import seller_middleware
from ..database.db import Database
from typing import Optional

if path.exists(path.join(path.dirname(__file__), "..", "..", ".env")):
    from dotenv import load_dotenv
    load_dotenv(path.join(path.dirname(__file__), "..", "..", ".env"))


def product_middleware(request: Request) -> SellerPayloadModel:
    sellerPayload: SellerPayloadModel = seller_middleware(request)
    product_id_str: str | None = request.path_params.get("product_id")
    product_id: Optional[int] = None
    if not product_id_str:
        raise HTTPException(status_code=400, detail="Product id is required.")
    try:
        product_id = int(product_id_str)
    except:
        raise HTTPException(status_code=400, detail="Product id must be a number.")
    if not product_id in Database.fetchOne("id", "products", f"seller_id = {sellerPayload['seller_id']}"):
        raise HTTPException(status_code=400, detail="You are not authorized to access this product.")
    return sellerPayload
