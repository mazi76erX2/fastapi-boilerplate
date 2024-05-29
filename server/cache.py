"""
Description: This file contains the RedisCache class which is used to
interact with the Redis cache.
"""

from typing import Optional

import aioredis

from config import REDIS_URL


class RedisCache:
    """Redis cache class"""

    def __init__(self, url: str):
        self.url = url
        self.redis = None

    async def connect(self):
        """Connect to Redis"""
        self.redis = await aioredis.create_redis_pool(self.url, encoding="utf-8")

    async def close(self):
        """Close the Redis connection"""
        self.redis.close()
        await self.redis.wait_closed()

    async def get(self, key: str) -> Optional[str]:
        """Get value from Redis cache"""
        return await self.redis.get(key)

    async def set(self, key: str, value: str, expire: int = 3600):
        """Set value in Redis cache"""
        await self.redis.set(key, value, expire=expire)

    async def delete(self, key: str):
        """Delete value from Redis cache"""
        await self.redis.delete(key)


redis_cache = RedisCache(REDIS_URL)
