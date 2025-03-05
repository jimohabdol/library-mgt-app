from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from app.models import User, Book, BorrowedBook

async def init_db(mongo_uri: str):
    client = AsyncIOMotorClient(mongo_uri)
    await init_beanie(database=client.library, document_models=[User, Book, BorrowedBook])