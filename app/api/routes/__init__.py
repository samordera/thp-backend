from fastapi import APIRouter
from app.controllers import MainController

router = APIRouter()

@router.get("/")
async def get_root():
  return await MainController.root()