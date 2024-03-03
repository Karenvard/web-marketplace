from pydantic import BaseModel, validator
from fastapi import HTTPException, UploadFile

from database.db import Database

class ProductModel(BaseModel):
    title: str
    description: str
    price: float
    image: UploadFile
    type_id: int
    brand_id: int

    @validator("title")
    def validate_title(cls, value: str) -> str:
        if not value:
            raise HTTPException(status_code=400, detail="Title is required.")
        elif (len(value) < 3):
            raise HTTPException(status_code=400, detail="Title is too short, must be at least 3.")
        elif (len(value) > 50):
            raise HTTPException(status_code=400, detail="Title is too long.")
        return value
    
    @validator("description")
    def validate_description(cls, value: str) -> str:
        if not value:
            raise HTTPException(status_code=400, detail="Description is required.")
        elif (len(value) < 20):
            raise HTTPException(status_code=400, detail="Description is too short, must be at least 20.")
        elif (len(value) > 255):
            raise HTTPException(status_code=400, detail="Description is too long.")
        return value
    
    @validator("price")
    def validate_price(cls, value: float) -> float:
        if not value:
            raise HTTPException(status_code=400, detail="Price is required.")
        elif (value < 0):
            raise HTTPException(status_code=400, detail="Price cannot be negative.")
        return value
    
    @validator("image")
    def validate_image(cls, value: UploadFile) -> UploadFile:
        if not value:
            raise HTTPException(status_code=400, detail="Image is required.")
        return value

    @validator("type_id")
    def check_type_id(cls, type_id: int) -> int:
        for tuple in Database.fetchAll("SELECT id FROM types"):
            if type_id not in tuple:
                raise HTTPException(status_code=400, detail="Invalid type ID.")
        return type_id

    @validator("brand_id")
    def check_brand_id(cls, brand_id: int) -> int:
        for tuple in Database.fetchAll("SELECT id FROM brands"):
            if brand_id not in tuple:
                raise HTTPException(status_code=400, detail="Invalid brand ID.")
        return brand_id


