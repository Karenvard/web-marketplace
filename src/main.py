'''
Author: Karen Vardanian (vkaren1777@icloud.com)
File Created: Thursday, 22nd February 2024 8:20:16 pm
Copyright © 2024 - Karen Vardanian
'''


from fastapi import FastAPI
from .routers.main_router import main_router
from .database.db import Database

app: FastAPI = FastAPI()
app.include_router(prefix="/api", router=main_router)

if __name__ == "__main__":
    import uvicorn
    Database.setup()
    uvicorn.run(app, host="0.0.0.0", port=8000)
