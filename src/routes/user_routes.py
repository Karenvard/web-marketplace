'''
Author: Karen Vardanian (vkaren1777@icloud.com)
File Created: Thursday, 22nd February 2024 8:40:04 pm
Copyright © 2024 - Karen Vardanian
'''


from fastapi import APIRouter
from handlers.user_handler import UserHandler

userRouter: APIRouter = APIRouter()

userRouter.add_api_route("/signup", UserHandler.signup, methods=["POST"])
userRouter.add_api_route("/signin", UserHandler.signin, methods=["POST"])
userRouter.add_api_route("/getauthenticated", UserHandler.getAuthenticatedUser, methods=["GET"])
#userRouter.add_api_route("/changeInfo", UserHandler.changeInfo, methods=["PUT"])