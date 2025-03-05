from sqlalchemy.orm import Session
from . import models

def create_book(db: Session, book: BookCreate):
    db_book = models.Book(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def delete_book(db: Session, book_id: int):
    db_book = db.query(models.Book).filter(models.Book.id == book_id).first()
    db_book.is_deleted = True
    db.commit()
    return db_book

def get_users(db: Session):
    return db.query(models.User).all()

def get_borrowed_books(db: Session):
    return db.query(models.BorrowedBook).all()