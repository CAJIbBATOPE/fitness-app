from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
import os

app = FastAPI()

mongodb_url = os.getenv("MONGODB_URL", "mongodb://localhost:27017")
client = AsyncIOMotorClient(mongodb_url)
db = client.fitnessdb

@app.get("/")
async def root():
    try:
        # Тестове підключення
        await db.command("ping")
        db_status = "MongoDB connected ✅"
    except Exception as e:
        db_status = f"MongoDB connection failed: {e}"

    return {
        "message": "Фітнес-додаток працює!",
        "database_status": db_status
    }
