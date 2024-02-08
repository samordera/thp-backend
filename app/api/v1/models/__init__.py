from pydantic import BaseModel

class UserData(BaseModel):
  firstName: str | None = None
  lastName: str | None = None
  email: str | None = None
  username: str | None = None
  password: str