from pydantic import BaseModel, validator
from fastapi import HTTPException

class SellerModel(BaseModel):
    name: str
    description: str

    @validator("name")
    def validate_name(cls, value: str) -> str:
        if not value:
            raise HTTPException(status_code=400, detail="Name is required.")
        elif (len(value) < 4):
            raise HTTPException(status_code=400, detail="Name is too short, must be at least 4.")
        elif (len(value) > 50):
            raise HTTPException(status_code=400, detail="Name is too long.")
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
 
