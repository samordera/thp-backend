from fastapi.middleware.cors import CORSMiddleware
from app import app_

origins = [
  "*",
  # Frontend origin for requests with credentials
]

app_.add_middleware(
  CORSMiddleware,
  allow_origins=origins,
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"]
)