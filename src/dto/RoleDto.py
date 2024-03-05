from pydantic import BaseModel, validator

class RoleDto(BaseModel):
    name: str


    @validator("name")
    def validate_name(cls, value: str) -> str:
        if not value:
            raise ValueError("Name is required.")
        elif (len(value) < 1):
            raise ValueError("Name is too short, must be at least 3.")
        elif (len(value) > 80):
            raise ValueError("Name is too long.")
        return value
