from pydantic import BaseModel
from datetime import datetime

class UserCreate(BaseModel):
    email: str
    firstname: str
    lastname: str

class BookResponse(BaseModel):
    id: str
    title: str
    author: str
    publisher: str
    category: str
    is_available: bool
    available_from: datetime | None

class BorrowRequest(BaseModel):
    duration_days: int