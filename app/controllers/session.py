from app.services.session import SessionServices
from app.controllers import oauth2_scheme
from fastapi import Depends

class SessionController:
  def __init__():
    pass
  
  async def create(access_token: str=Depends(oauth2_scheme)):
    try:
      return {
        "success": True,
        "message": "New session was created"
      }
    except:
      return {
        "success": False,
        "message": "There was an error creating session"
      }   
  
  async def active():
    try:
      session_active = SessionServices.active()
      return {
        "success": True,
        "session active": session_active,
        "message": "There is an active session" if session_active else "There is no active session"
      }
    except:
      return {
        "success": False,
        "message": "There was an error checking for an active session"
      }      
  
  async def get_history(session_id: str, access_token: str=Depends(oauth2_scheme)):
    try:
      return {
        "success": True,
        "session history": {}
      }
    except:
      return {
        "success": False,
        "message": "There was an error getting session history"
      }
  
  async def update_history(session_id: str, access_token: str=Depends(oauth2_scheme)):
    try:
      return {
        "success": True,
        "message": "Session history was was updated"
      }
    except:
      return {
        "success": False,
        "message": "There was an error updating session history"
      }
  
  async def terminate(session_id: str, access_token: str=Depends(oauth2_scheme)):
    try:
      return {
        "success": True,
        "message": "Session was terminated"
      }
    except:
      return {
        "success": False,
        "message": "There was an error terminating session"
      }
  