import os
from motor.motor_asyncio import AsyncIOMotorClient

mongodb_url = os.getenv("MONGODB_URL", "mongodb://mongodb:27017")
client = AsyncIOMotorClient(mongodb_url)
db = client.fitnessdb
