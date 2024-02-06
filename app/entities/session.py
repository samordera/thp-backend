from typing import List
from datetime import datetime

class Action:
  def __init__(self, active_module: str | None, name: str):
    self.name = name
    self.active_module = active_module | None
    self.time = datetime.now()

  def get_action(self):
    return {
      self.name,
      self.active_module,
      self.time
    }

class Session:
  def __init__(self, id: str, history: List[Action]=[]):
    self.id = id
    self.history = history
    pass

  def __enter__():
    pass

  def __exit__():
    pass

  def get_history(self):
    return self.history
  
  def update_history(self, new_action: Action):
    self.history.append(new_action)
    return self.get_history()