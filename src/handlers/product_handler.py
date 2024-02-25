from database.db import Database
from fastapi import Depends, HTTPException
from middlewares.auth_middleware import auth_middleware
from models import addProductModel
from models import PayloadModel

class ProductHandler:
    def addProduct(product: addProductModel, payload: PayloadModel.model_dump = Depends(auth_middleware)) -> None:
        sellerId = Database.fetchOne("id", "sellers", f"user_id = {payload['id']}")[0]
        if not sellerId:
            raise HTTPException(status_code=400, detail="You are not a seller.")
        Database.insertInto("products", "title, description, price, type_id, brand_id, color_id, seller_id", f"'{product.title}', '{product.description}', '{product.price}', '{product.type_id}', '{product.brand_id}', '{product.color_id}', '{sellerId}'")


    def changeProduct(updatedProduct: addProductModel, payload: PayloadModel.model_dump = Depends(auth_middleware)) -> None:
        pass