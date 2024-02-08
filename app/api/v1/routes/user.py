from fastapi import APIRouter
from app.controllers.user import UserController
from app.api.v1.models import UserData

router = APIRouter()

@router.get("/")
async def get_users():
  return await UserController.get_users()

@router.post("/")
async def create(user_data: UserData | None):
  return await UserController.create(user_data)

@router.post("/auth")
async def login(user_data: UserData | None):
  return await UserController.login(user_data)

@router.get("/{id}/logout")
async def logout(id: str, access_token: str):
  return await UserController.logout(id, access_token)

@router.post("/{id}")
async def update(id: str, user_data: UserData | None, access_token: str):
  return await UserController.update(id, user_data, access_token)

@router.post("/{id}")
async def delete(id: str, user_data: UserData | None, access_token: str):
  return await UserController.delete(id, user_data, access_token)