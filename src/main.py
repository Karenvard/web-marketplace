'''
Author: Karen Vardanian (vkaren1777@icloud.com)
File Created: Thursday, 22nd February 2024 8:20:16 pm
Copyright © 2024 - Karen Vardanian
'''


from fastapi import FastAPI
from routes.main_router import main_router
from database.db import Database

app: FastAPI = FastAPI()
app.include_router("/api", main_router)

print(Database.cur)
Database.setup()
print(Database.cur)

@app.get("/")
def index() -> str:
    return "index"

