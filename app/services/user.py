from app.entities.user import User
from app.services.session import SessionServices
from datetime import timedelta
import jwt
from passlib.context import CryptContext


class UserServices:
  async def create(user_data):
    user = User(user_data)
    return user

  async def get_users():
    users = []
    return users
  
  async def get_current_user(access_token):
    pass
  
  async def auth(user_data: User):
    '''
    This authenticates the user and creates a session using the SessionServices class
    '''
    pass

  async def logout(id: str):
    '''
    This invalidates the user's auth token and ends the current session
    '''
    pass

  async def update(user_data: User):
    '''
    This updates user data in the db 
    '''
    pass
  
  async def delete(id: str, user_data: User):
    '''
    This deletes a user from the db
    '''
    pass

  async def generate_access_token(user_data: User, token_expiration_delta: timedelta | None):
    '''
    A token generated using the jwt module (imported above) is to be returned
    '''
    pass

  async def verify_password(password: str, hashed_password: str):
    '''
    This retrieves the stored password hash in the db to verify the password string in user_data
    Using the CryptContext class imported above in recommended
    '''
    pass
