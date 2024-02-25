'''
Author: Karen Vardanian (vkaren1777@icloud.com)
File Created: Friday, 23rd February 2024 9:31:37 pm
Copyright © 2024 - Karen Vardanian
'''


from database.db import Database
from fastapi import Depends
from middlewares.auth_middleware import auth_middleware
from models import createSellerModel, PayloadModel, addProductModel

class SellerHandler:

    def create(seller: createSellerModel, payload: PayloadModel.model_dump = Depends(auth_middleware)) -> None:
        pass
        

    def delete() -> None:
        pass