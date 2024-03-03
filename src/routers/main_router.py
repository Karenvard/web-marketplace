'''
Author: Karen Vardanian (vkaren1777@icloud.com)
File Created: Thursday, 22nd February 2024 9:03:09 pm
Copyright © 2024 - Karen Vardanian
'''


from fastapi import APIRouter
from .user_router import user_router
from .seller_router import seller_router
from .product_router import product_router
from .type_router import type_router
from .brand_router import brand_router
from .role_router import role_router
from .basket_router import basket_router

main_router: APIRouter = APIRouter()

main_router.include_router(user_router, prefix="/user")
main_router.include_router(seller_router, prefix="/seller")
main_router.include_router(product_router, prefix="/product")
main_router.include_router(type_router, prefix="/type")
main_router.include_router(brand_router, prefix="/brand")
main_router.include_router(role_router, prefix="/role")
main_router.include_router(basket_router, prefix="/basket")
