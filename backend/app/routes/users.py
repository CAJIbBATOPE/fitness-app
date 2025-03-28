from fastapi import APIRouter, HTTPException, Depends
from app.database import db
from app.models import User
from app.schemas import UserCreate
from app.auth import get_password_hash

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", response_model=User)
async def create_user(user: UserCreate):
    existing_user = await db.users.find_one({"email": user.email})
    if existing_user:
        raise HTTPException(status_code=400, detail="Email вже зареєстрований")
    hashed_password = get_password_hash(user.password)
    user_data = user.dict()
    user_data["hashed_password"] = hashed_password
    user_data.pop("password")
    new_user = await db.users.insert_one(user_data)
    created_user = await db.users.find_one({"_id": new_user.inserted_id})
    created_user["id"] = str(created_user["_id"])
    return created_user
