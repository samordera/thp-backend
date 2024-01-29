from fastapi import FastAPI
from app.api.routes import router

server = FastAPI()

server.include_router(router)