from fastapi import APIRouter
from fastapi import APIRouter
from ..handlers.role_handler import role_handler
role_router: APIRouter = APIRouter()


role_router.add_api_route("/add", role_handler.add, methods=["POST"])
role_router.add_api_route("/get/{role_id}", role_handler.get, methods=["GET"])
role_router.add_api_route("/update/{role_id}", role_handler.update, methods=["PUT"])
role_router.add_api_route("/give/{role_id}", role_handler.give, methods=["POST"])
role_router.add_api_route("/getall", role_handler.get_all, methods=["GET"])
role_router.add_api_route("/delete/{role_id}", role_handler.delete, methods=["DELETE"])
