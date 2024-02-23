
from pydantic import BaseModel

class BrandModel(BaseModel):
    id: int
    name: str