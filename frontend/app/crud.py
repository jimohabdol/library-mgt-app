from app.models import User, Book, BorrowedBook
from beanie.odm.operators.find.logical import And

async def create_user(user: User) -> User:
    return await user.insert()

async def get_books(publisher: str = None, category: str = None):
    query = []
    if publisher:
        query.append(Book.publisher == publisher)
    if category:
        query.append(Book.category == category)
    return await Book.find(And(*query), fetch_links=True).to_list()

async def borrow_book(book_id: str, user: User, duration_days: int):
    book = await Book.get(book_id)
    if not book.is_available:
        return None
    
    book.is_available = False
    await book.save()
    
    borrowed = BorrowedBook(user=user, book=book, duration_days=duration_days)
    return await borrowed.insert()