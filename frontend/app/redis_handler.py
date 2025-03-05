import aioredis
import json
from app.models import Book
from app.database import init_db

async def setup_redis_subscriber(mongo_uri: str):
    redis = aioredis.from_url("redis://redis:6379")
    pubsub = redis.pubsub()
    await pubsub.subscribe("book_added", "book_removed")
    
    async for message in pubsub.listen():
        if message["type"] == "message":
            channel = message["channel"].decode()
            data = json.loads(message["data"])
            
            if channel == "book_added":
                book = Book(**data)
                await book.insert()
            elif channel == "book_removed":
                await Book.find_one(Book.id == data["id"]).delete()