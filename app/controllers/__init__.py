from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


class MainController:
  def __init__():
    pass

  async def root():
    return {
      "success": True,
      "message": "Server is live!"
    }