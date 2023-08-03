from pydantic import BaseModel, EmailStr
from datetime import datetime

class sendMessage(BaseModel):
    username: str
    title: str
    content: str

class getMessage(BaseModel):
    sent_at: datetime