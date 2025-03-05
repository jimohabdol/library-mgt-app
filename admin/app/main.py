from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import get_db, Base, engine
from .redis_handler import setup_redis_subscriber
import os

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.on_event("startup")
async def startup():
    db = next(get_db())
    await setup_redis_subscriber(db)

@app.post("/admin/books/", response_model=schemas.BookCreate)
def add_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    return crud.create_book(db, book)

@app.delete("/admin/books/{book_id}")
def remove_book(book_id: int, db: Session = Depends(get_db)):
    return crud.delete_book(db, book_id)

@app.get("/admin/users/", response_model=list[schemas.UserResponse])
def list_users(db: Session = Depends(get_db)):
    return crud.get_users(db)

@app.get("/admin/borrowed-books/", response_model=list[schemas.BorrowedBookResponse])
def list_borrowed_books(db: Session = Depends(get_db)):
    return crud.get_borrowed_books(db)