import aioredis
import json
from sqlalchemy.orm import Session
from . import models

async def setup_redis_subscriber(db: Session):
    redis = aioredis.from_url("redis://redis:6379")
    pubsub = redis.pubsub()
    await pubsub.subscribe("user_created", "book_borrowed")
    
    async for message in pubsub.listen():
        if message["type"] == "message":
            channel = message["channel"].decode()
            data = json.loads(message["data"])
            
            if channel == "user_created":
                user = models.User(**data)
                db.add(user)
                db.commit()
            elif channel == "book_borrowed":
                borrowed = models.BorrowedBook(**data)
                db.add(borrowed)
                db.commit()