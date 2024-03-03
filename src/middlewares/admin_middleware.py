from fastapi import Request, HTTPException
from database.db import Database
from ..models.PayloadModel import PayloadModel
from .auth_middleware import auth_middleware

def admin_middleware(request: Request) -> PayloadModel:
    payload: PayloadModel = auth_middleware(request)
    dbAdminRoleId: int = Database.fetchOne("id", "roles", f"name = 'ADMIN'")[0]
    userRoleId: int = Database.fetchOne("role_id", "users", f"id = {payload['id']}")[0]
    if not dbAdminRoleId == userRoleId:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return payload
