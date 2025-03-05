from pydantic import BaseModel
from datetime import datetime

class BookCreate(BaseModel):
    title: str
    author: str
    publisher: str
    category: str

class UserResponse(BaseModel):
    email: str
    firstname: str
    lastname: str
    enrolled_at: datetime

class BorrowedBookResponse(BaseModel):
    user_id: int
    book_id: int
    borrowed_date: datetime
    duration_days: int