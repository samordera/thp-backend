from app.services.user import UserServices
from fastapi import Depends
from app.controllers import oauth2_scheme


class UserController:
  def __init__():
    pass
  
  async def get_users():
    try:
      users = await UserServices.get_users()
      return {
        "success": True,
        "message": "Users retrieved",
        "users": users
      }
    except:
      return {
        "success": False,
        "message": "There was an error while trying to get users"
      }

  async def create(user_data):
    try:
      user = await UserServices.create(user_data)
      print(f'User created - {user}')
      return {
        "success": True,
        "message": "New user was created"
      }
    except:
      return {
        "success": False,
        "message": "There was an error while trying to create user"
      }
    
  async def login(user_data):
    try:
      await UserServices.auth(user_data)
      return {
        "success": True,
        "message": "Login successful"
      }
    except:
      return {
        "success": False,
        "message": "There was an error while trying to log in"
      }
  
  async def logout(id: str, access_token: str=Depends(oauth2_scheme)):
    try:
      await UserServices.logout(id)
      return {
        "success": True,
        "message": "Logout successful"
      }
    except:
      return {
        "success": False,
        "message": "There was an error while trying to log out"
      }
    
  async def update(id: str, access_token: str=Depends(oauth2_scheme)):
    try:
      return {
        "success": True,
        "message": "User was was updated"
      }
    except:
      return {
        "success": False,
        "message": "There was an error while trying to update user"
      }
  
  async def delete(id, user_data, access_token: str=Depends(oauth2_scheme)):
    try:
      return {
        "success": True,
        "message": "User was deleted"
      }
    except:
      return {
        "success": False,
        "message": "There was an error while trying to delete user"
      }
  