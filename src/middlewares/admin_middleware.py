from fastapi import Request, HTTPException
from database.db import Database
from models.PayloadModel import PayloadModel
from .auth_middleware import auth_middleware

def admin_middleware(request: Request) -> PayloadModel:
    payload: PayloadModel = auth_middleware(request)
    db_admin_role_id: int = Database.fetchOne("SELECT role_id FROM roles WHERE name = 'ADMIN'")[0]
    user_role_id: int = Database.fetchOne(f"SELECT role_id FROM users WHERE id = {payload['id']}")[0]
    if not db_admin_role_id == user_role_id:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return payload
