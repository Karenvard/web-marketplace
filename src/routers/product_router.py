'''
Author: Karen Vardanian (vkaren1777@icloud.com)
File Created: Friday, 23rd February 2024 9:28:57 pm
Copyright © 2024 - Karen Vardanian
'''



from fastapi import APIRouter
from ..handlers.product_handler import product_handler
product_router: APIRouter = APIRouter()


product_router.add_api_route("/add", product_handler.add, methods=["POST"])
product_router.add_api_route("/update/{product_id}", product_handler.update, methods=["PUT"])
product_router.add_api_route("/get/{product_id}", product_handler.get, methods=["GET"])
product_router.add_api_route("/getall", product_handler.get_all, methods=["GET"])
product_router.add_api_route("/delete/{product_id}", product_handler.delete, methods=["DELETE"])
product_router.add_api_route("/rate/{product_id}", product_handler.rate, methods=["POST"])
product_router.add_api_route("/get_rating/{product_id}", product_handler.get_ratings, methods=["GET"])
