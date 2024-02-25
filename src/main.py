'''
Author: Karen Vardanian (vkaren1777@icloud.com)
File Created: Thursday, 22nd February 2024 8:20:16 pm
Copyright © 2024 - Karen Vardanian
'''


from fastapi import FastAPI, middleware, Request
from routes.main_router import main_router
from database.db import Database

app: FastAPI = FastAPI()
app.include_router(prefix="/api", router=main_router)


Database.setup()


@app.get("/")
def index(request: Request) -> str:
    return f"{request.headers.get('user-agent')}"

