from pydantic import BaseModel, EmailStr
from datetime import datetime

class UserCreateResponseModel(BaseModel):
    username: str
    id: int
    
    class Config:
            orm_mode = True

class sendMessageInput(BaseModel):
    from_user : str
    to_user : str
    title: str
    content: str

class getMessage(sendMessageInput):
    sent_at: datetime

class UserCreateInput(BaseModel):
    username: str
    password: str
