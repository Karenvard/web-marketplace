'''
Author: Karen Vardanian (vkaren1777@icloud.com)
File Created: Thursday, 22nd February 2024 8:40:04 pm
Copyright © 2024 - Karen Vardanian
'''


from fastapi import APIRouter
from handlers.user_handler import user_handler

user_router: APIRouter = APIRouter()

user_router.add_api_route("/signup", user_handler.signup, methods=["POST"])
user_router.add_api_route("/signin", user_handler.signin, methods=["POST"])
user_router.add_api_route("/authenticated", user_handler.get_authenticated, methods=["GET"])
user_router.add_api_route("/update", user_handler.update, methods=["PUT"])
user_router.add_api_route("/get/{user_id}", user_handler.get, methods=["GET"])
user_router.add_api_route("/delete", user_handler.delete, methods=["DELETE"])
