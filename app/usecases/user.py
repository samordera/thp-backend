from app.entities.user import User

class UserUsecases:
  async def create(user_data):
    user = User(user_data)
    return user

  async def get_users():
    users = []
    return users
  
  async def login():
    pass

  async def logout():
    pass