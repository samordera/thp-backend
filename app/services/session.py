from typing import List
from app.entities.session import Session
from app.entities.session import Action
from app.entities.user import User
from app.services.user import UserServices
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class SessionServices:
  async def create(access_token: str):
    '''
    This creates a new session using a generated access token for user
    '''

  async def active():
    '''
    Returns true if there is an active session and false if not
    '''
    session_active = False
    return session_active

  async def get_history(session_id: str, access_token: str):
    '''
    This returns the history for the session with id, session_id
    '''
    Session.get_history(session_id)
    return
  
  async def update_history(session_id: str, current_history: List[Action], action: Action):
    '''
    This recieves an action of type Action, defined in entities, and the session history, updates the session history and saves the new entry in the db 
    '''
    session = Session(history=current_history)
    session.update_history(action)
    return
  
  async def validate_token(access_token: str):
    '''
    This validates the bearer auth access token for protected endpoints
    All protected routes use oauth 2.0 scheme for token validation
    '''
    pass