'''
Author: Karen Vardanian (vkaren1777@icloud.com)
File Created: Friday, 23rd February 2024 9:28:57 pm
Copyright © 2024 - Karen Vardanian
'''



from fastapi import APIRouter
from handlers.seller_handler import seller_handler
seller_router: APIRouter = APIRouter()

seller_router.add_api_route("/create", seller_handler.create, methods=["POST"])
seller_router.add_api_route("/update", seller_handler.update, methods=["PUT"])
seller_router.add_api_route("/getauthenticated", seller_handler.get_authenticated, methods=["GET"])
seller_router.add_api_route("/get/{seller_id}", seller_handler.get, methods=["GET"])
seller_router.add_api_route("/delete", seller_handler.delete, methods=["DELETE"])
