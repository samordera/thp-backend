from app.usecases.user import UserUsecases

class UserController:
  def __init__():
    pass
  
  async def get_users():
    try:
      users = UserUsecases.get_users()
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
      user = await UserUsecases.create(user_data)
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
      await UserUsecases.login(user_data)
      return {
        "success": True,
        "message": "Login successful"
      }
    except:
      return {
        "success": False,
        "message": "There was an error while trying to log in"
      }
  
  async def logout(id):
    try:
      await UserUsecases.logout(id)
      return {
        "success": True,
        "message": "Logout successful"
      }
    except:
      return {
        "success": False,
        "message": "There was an error while trying to log out"
      }
    
  async def update(id):
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
  
  async def delete(id, user_data):
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
  