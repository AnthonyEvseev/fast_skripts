from fastapi import FastAPI
import uvicorn
from core.config import HOST, PORT
from app.api import chat_router

app = FastAPI()

app.include_router(chat_router, tags=["Chat"])

if __name__ == '__main__':
    uvicorn.run(app, host=HOST, port=PORT)
