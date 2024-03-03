from fastapi import APIRouter
from ..handlers.basket_handler import basket_handler
basket_router: APIRouter = APIRouter()


basket_router.add_api_route("/addProduct/{product_id}", basket_handler.add_product, methods=["POST"])
basket_router.add_api_route("/getall", basket_handler.get_all, methods=["GET"])
basket_router.add_api_route("/deleteProduct/{product_id}", basket_handler.delete_product, methods=["DELETE"])
