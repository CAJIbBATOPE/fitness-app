from fastapi import FastAPI
from app.database import db
from app.routes import users

app = FastAPI()

app.include_router(users.router)

@app.get("/")
async def root():
    try:
        await db.command("ping")
        db_status = "MongoDB connected ✅"
    except Exception as e:
        db_status = f"MongoDB connection failed: {e}"

    return {
        "message": "Фітнес-додаток працює!",
        "database_status": db_status
    }

