import json
import redis.asyncio as redis
from src.tron_app.schema import WalletResponse

redis_client = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)


async def get_cache_data(name:str):
    stored_data = await redis_client.get(name)
    if stored_data:
        data = json.loads(stored_data)
        return {"status": True, "data": data}
    return {"status": False, "message": "No data found"}

async def set_cache_data(name:str, data:list[WalletResponse]):
    redis_client.set("my_dicts", json.dumps(data))
    return {"status": "success", "message": "Data saved to Redis"}

async def delete_cache_data(name:str):
    await redis_client.delete(name)
    return {"status": "success", "message": "Data deleted from Redis"}
