from app.entities.session import Session

class User:
  def __init__(self, firstName: str, lastName: str, username: str, email: str, password: str, last_session: Session | None):
    self.firstName = firstName
    self.lastName = lastName
    self.username = username
    self.email = email
    self.password = password
    self.last_session = last_session
    self.is_new_user = True if last_session == None else False

  def get_user_details(self):
    return {
      self.firstName,
      self.lastName,
      self.username,
      self.email,
      self.password
    }