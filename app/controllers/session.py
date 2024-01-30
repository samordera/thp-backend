from app.usecases.session import SessionUsecases

class SessionController:
  def __init__():
    pass
  
  async def create():
    return {
      "success": True,
      "message": "New session was created"
    }
  
  async def active():
    session_active = SessionUsecases.active()
    return {
      "success": True,
      "session active": session_active,
    }
  
  async def get_history():
    return {
      "success": True,
      "session history": {}
    }
  
  async def update_history(id):
    return {
      "success": True,
      "message": "Session history was was updated"
    }
  
  async def terminate(id):
    return {
      "success": True,
      "message": "Session was terminated"
    }
  