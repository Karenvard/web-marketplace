from pydantic import BaseModel

class ProductModel(BaseModel):
    id: int
    name: str
    description: str
    price: float
    brand: str
    type: str
    seller: int
    created: str
    color: str