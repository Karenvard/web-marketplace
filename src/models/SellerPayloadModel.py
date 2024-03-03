from typing import Optional, TypedDict

class SellerPayloadModel(TypedDict):
    id: int
    fullname: str
    email: str
    seller_id: Optional[int]


