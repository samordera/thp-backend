from fastapi import APIRouter
from app.controllers.user import UserController

###
# The following code should go in a separate file
from pydantic import BaseModel
class UserData(BaseModel):
  # JSON schema for user data
  pass
###

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
async def logout(id: str):
  return await UserController.logout(id)

@router.post("/{id}")
async def update(id: str, user_data: UserData | None):
  return await UserController.update(id, user_data)

@router.post("/{id}")
async def delete(id: str, user_data: UserData | None):
  return await UserController.delete(id, user_data)