from fastapi import APIRouter
from app.controllers import MainController

from app.api.v1.routes.user import router as user_router
from app.api.v1.routes.session import router as session_router
from app.api.v1.routes.data_analysis.table import router as table_router

api_router = APIRouter()
api_router.include_router(user_router, prefix="/api/users")
api_router.include_router(session_router, prefix="/api/session")
api_router.include_router(table_router, prefix="/api/tables")

@api_router.get("/")
async def get_root():
  return await MainController.root()

@api_router.get("/api")
async def get_root():
  return await get_root()