
from typing import List
from pydantic import BaseModel


class SellerModel(BaseModel):
    id: int
    owner: int
    name: str
    description: str
    created: str
    products: List[int]