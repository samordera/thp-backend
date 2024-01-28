from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def default_entry_point():
  print("Server running")
  return {
    "success": True,
    "message": "server is live"
  }