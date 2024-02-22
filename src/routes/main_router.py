from fastapi import APIRouter
from src.routes.user_routes import userRouter

main_router: APIRouter = APIRouter()

main_router.include_router(userRouter, prefix="/user")