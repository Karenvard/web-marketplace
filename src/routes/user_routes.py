from fastapi import APIRouter
from src.handlers.user_handler import UserHandler

userRouter: APIRouter = APIRouter()

userRouter.add_api_route("/signup", UserHandler.signup, methods=["POST"])
userRouter.add_api_route("/signin", UserHandler.signin, methods=["POST"])