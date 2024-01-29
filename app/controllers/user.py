class UserController:
  def __init__():
    pass
  
  async def get_all_users():
    return {
      "success": True,
      "message": "Users retrieved"
    }

  async def create(user_data):
    return {
      "success": True,
      "message": "New user was created"
    }
  
  
  async def update(id):
    return {
      "success": True,
      "message": "User was was updated"
    }
  
  async def delete(id):
    return {
      "success": True,
      "message": "User was deleted"
    }
  