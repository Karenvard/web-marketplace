from dataclasses import dataclass
from datetime import datetime

@dataclass
class ProductModel:
    id: int
    title: str
    description: str
    image: str
    price: float
    type_id: int
    brand_id: int
    seller_id: int
    rating_id: int
    created: datetime
