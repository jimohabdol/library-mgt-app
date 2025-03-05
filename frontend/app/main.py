from fastapi import FastAPI, HTTPException
from app.models import User, Book, BorrowedBook
from app.schemas import UserCreate, BookResponse, BorrowRequest
from app.crud import create_user, get_books, borrow_book
from app.database import init_db
from app.redis_handler import setup_redis_subscriber
import os

app = FastAPI()

@app.on_event("startup")
async def startup():
    mongo_uri = os.getenv("MONGO_URI", "mongodb://frontend-db:27017")
    await init_db(mongo_uri)
    await setup_redis_subscriber(mongo_uri)

@app.post("/users/", response_model=UserCreate)
async def enroll_user(user: UserCreate):
    db_user = await User(**user.dict()).insert()
    return db_user

@app.get("/books/", response_model=list[BookResponse])
async def list_books(publisher: str = None, category: str = None):
    return await get_books(publisher, category)

@app.post("/books/{book_id}/borrow")
async def borrow_book(book_id: str, request: BorrowRequest):
    # In real implementation, get user from auth
    user = await User.find_one()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    borrowed = await borrow_book(book_id, user, request.duration_days)
    if not borrowed:
        raise HTTPException(status_code=400, detail="Book not available")
    return {"message": "Book borrowed successfully"}