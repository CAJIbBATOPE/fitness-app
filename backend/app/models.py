from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

# Користувач
class User(BaseModel):
    id: Optional[str]
    email: EmailStr
    hashed_password: str
    full_name: Optional[str] = None
    created_at: datetime = datetime.utcnow()

# Вправа
class Exercise(BaseModel):
    id: Optional[str]
    name: str
    description: Optional[str] = None
    duration_minutes: int
    calories_burned: Optional[int] = None
    created_at: datetime = datetime.utcnow()

# Харчування
class Nutrition(BaseModel):
    id: Optional[str]
    name: str
    calories: int
    proteins: Optional[float] = None
    carbs: Optional[float] = None
    fats: Optional[float] = None
    created_at: datetime = datetime.utcnow()
