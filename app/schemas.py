from pydantic import BaseModel, EmailStr
from datetime import datetime

class sendMessage(BaseModel):
    from_user : str
    to_user : str
    title: str
    content: str

class getMessage(sendMessage):
    sent_at: datetime

class UserCreate(BaseModel):
    username: str
    password: str