from fastapi import APIRouter
from fastapi import APIRouter
from ..handlers.type_handler import type_handler
type_router: APIRouter = APIRouter()


type_router.add_api_route("/add", type_handler.add, methods=["POST"])
type_router.add_api_route("/get/{type_id}", type_handler.get, methods=["GET"])
type_router.add_api_route("/update/{type_id}", type_handler.update, methods=["PUT"])
type_router.add_api_route("/getall", type_handler.get_all, methods=["GET"])
type_router.add_api_route("/delete/{type_id}", type_handler.delete, methods=["DELETE"])
