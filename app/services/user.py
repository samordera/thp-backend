from app.entities.user import User

class UserServices:
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

  async def update():
    pass
  
  async def delete():
    pass