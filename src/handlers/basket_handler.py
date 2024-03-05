from typing import Dict, List
from fastapi import Depends
from database.db import Database
from models.PayloadModel import PayloadModel
from middlewares.auth_middleware import auth_middleware
from fastapi import HTTPException
from models.ProductModel import ProductModel
from models.SuccessfulResponse import SuccessfulResponse


class basket_handler:

    @staticmethod
    def add_product(
        product_id: int, payload: PayloadModel = Depends(auth_middleware)
    ) -> SuccessfulResponse:
        # 1. check if product in basket with given id exists
        # 2. get product
        # 3. add product to basket
        # 4. return success message {"message": "Product was added to basket successfully."}
        if not product_id:
            raise HTTPException(status_code=400, detail="Product id is required.")
        if not Database.fetchOne(f"SELECT id FROM products WHERE id = {product_id}"):
            raise HTTPException(status_code=400, detail="Product not found.")
        basket_id = Database.fetchOne(
            f"SELECT id FROM baskets WHERE user_id = {payload['id']}"
        )[0]
        Database.commit(
            f"INSERT INTO basket_products (product_id, basket_id) VALUES ({product_id}, {basket_id})"
        )
        return {"message": "Product was added to basket successfully."}

    @staticmethod
    def get_all(
        page_number: int,
        page_size: int,
        payload: PayloadModel = Depends(auth_middleware),
    ) -> List[ProductModel]:
        # 1. get basket
        # 2. return basket
        if not page_number:
            raise HTTPException(status_code=400, detail="Page number is required.")

        if not page_size:
            raise HTTPException(status_code=400, detail="Page size is required.")
        elif page_size > 30:
            raise HTTPException(status_code=400, detail="Page size is too large.")
        offset: int = (page_number - 1) * page_size
        basket_id = Database.fetchOne(
            f"SELECT id FROM baskets WHERE user_id = {payload['id']}"
        )[0]
        db_products = Database.fetchAll(
            f"SELECT id, title, description, image, price, type_id, brand_id, seller_id, rating_id, created FROM basket_products WHERE basket_id = {basket_id} LIMIT {page_size} OFFSET {offset}"
        )
        products: List[ProductModel] = [
            ProductModel(
                id=product[0],
                title=product[1],
                description=product[2],
                image=product[3],
                price=product[4],
                type_id=product[5],
                brand_id=product[6],
                seller_id=product[7],
                rating_id=product[8],
                created=product[9],
            )
            for product in db_products
        ]
        return products

    @staticmethod
    def delete_product(product_id: int, payload: PayloadModel = Depends(auth_middleware)) -> SuccessfulResponse:
        # 1. check if product in basket with given id exists
        # 2. get product
        # 3. delete product from basket
        # 4. return success message {"message": "Product was deleted from basket successfully."}
        if not product_id:
            raise HTTPException(status_code=400, detail="Product id is required.")
        basket_id = Database.fetchOne(f"SELECT basket FROM baskets WHERE user_id = {payload['id']}")[0]
        Database.commit(f"DELETE FROM basket_products WHERE product_id = {product_id} AND basket_id = {basket_id}")
        return {"message": "Product was deleted from basket successfully."}
