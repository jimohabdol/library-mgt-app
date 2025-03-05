from datetime import datetime
from beanie import Document, Link
from pydantic import BaseModel

class User(Document):
    email: str
    firstname: str
    lastname: str
    enrolled_at: datetime = datetime.now()

    class Settings:
        name = "users"

class Book(Document):
    title: str
    author: str
    publisher: str
    category: str
    is_available: bool = True
    available_from: datetime | None = None

    class Settings:
        name = "books"

class BorrowedBook(Document):
    user: Link[User]
    book: Link[Book]
    borrowed_date: datetime = datetime.now()
    duration_days: int

    class Settings:
        name = "borrowed_books"