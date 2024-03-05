from typing import Optional, TypedDict

class SellerPayloadModel(TypedDict):
    id: int
    username: str
    seller_id: Optional[int]
    role_id: int


