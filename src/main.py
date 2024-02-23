'''
Author: Karen Vardanian (vkaren1777@icloud.com)
File Created: Thursday, 22nd February 2024 8:20:16 pm
Copyright © 2024 - Karen Vardanian
'''


from fastapi import FastAPI
from src.routes.main_router import main_router


app: FastAPI = FastAPI()
app.include_router(main_router)

@app.get("/")
def index() -> str:
    return "index"

