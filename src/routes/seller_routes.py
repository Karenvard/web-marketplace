'''
Author: Karen Vardanian (vkaren1777@icloud.com)
File Created: Friday, 23rd February 2024 9:28:57 pm
Copyright © 2024 - Karen Vardanian
'''



from fastapi import APIRouter
from handlers.seller_handler import SellerHandler
sellerRouter: APIRouter = APIRouter()

sellerRouter.add_api_route("/create", SellerHandler.create, methods=["POST"])
sellerRouter.add_api_route("/addProduct", SellerHandler.addProduct, methods=["POST"])
sellerRouter.add_api_route("/changeProduct", SellerHandler.changeProduct, methods=["POST"])
sellerRouter.add_api_route("/delete", SellerHandler.delete, methods=["DELETE"])