from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.api.v1.routes import api_router

@asynccontextmanager
async def server_init(server: FastAPI):
  server.include_router(api_router)
  yield

server = FastAPI(
  title="thp-backend-apiV1",
  lifespan=server_init
)