from fastapi import APIRouter
from handlers.brand_handler import brand_handler
brand_router: APIRouter = APIRouter()


brand_router.add_api_route("/add", brand_handler.add, methods=["POST"])
brand_router.add_api_route("/get/{brand_id}", brand_handler.get, methods=["GET"])
brand_router.add_api_route("/update/{brand_id}", brand_handler.update, methods=["PUT"])
brand_router.add_api_route("/getall", brand_handler.get_all, methods=["GET"])
brand_router.add_api_route("/delete/{brand_id}", brand_handler.delete, methods=["DELETE"])
