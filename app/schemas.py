from pydantic import BaseModel, EmailStr
from datetime import datetime

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

class UserCreateResponseModel(BaseModel):
    username: str