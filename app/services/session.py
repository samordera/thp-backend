from typing import List
from app.entities.session import Session
from app.entities.session import Action
from app.entities.user import User

class SessionServices:
  async def create(user_auth_data: User):
    SessionServices.generate_token(user_auth_data)
    print("session has been created")

  async def active():
    session_active = False
    return session_active
  
  async def generate_token(user: User):
    pass

  async def get_history(token: str, session_id: str):
    Session.get_history(session_id)
    return
  
  async def update_history(session_id: str, current_history: List[Action], action: Action):
    session = Session(history=current_history)
    session.update_history(action)
    return