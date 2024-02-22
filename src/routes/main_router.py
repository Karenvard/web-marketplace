'''
Author: Karen Vardanian (vkaren1777@icloud.com)
File Created: Thursday, 22nd February 2024 9:03:09 pm
Copyright © 2024 - Karen Vardanian
'''


from fastapi import APIRouter
from src.routes.user_routes import userRouter

main_router: APIRouter = APIRouter()

main_router.include_router(userRouter, prefix="/user")