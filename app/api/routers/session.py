from fastapi import APIRouter
from app.controllers.session import SessionController

session_router = APIRouter()

@session_router.get("/")
async def is_session_active():
  return await SessionController.active()

@session_router.get("/{id}")
async def get_session_history(id: str):
  return await SessionController.get_history(id)