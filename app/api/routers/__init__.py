from fastapi import APIRouter
from app.controllers import MainController

from app.api.routers.user import user_router
from app.api.routers.session import session_router
from app.api.routers.data_analysis.table import table_router

api_router = APIRouter()
api_router.include_router(user_router, prefix="/api/users")
api_router.include_router(session_router, prefix="/api/sessions")
api_router.include_router(table_router, prefix="/api/tables")

@api_router.get("/")
async def get_root():
  return await MainController.root()