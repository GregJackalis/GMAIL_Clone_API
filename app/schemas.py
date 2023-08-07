from pydantic import BaseModel, EmailStr
from datetime import datetime

class UserCreateResponseModel(BaseModel):
    username: str
    password: str
    
    class Config:
            from_attributes = True

class sendMessageInput(BaseModel):
    from_user : str
    to_user : str
    title: str
    content: str

class getMessage(sendMessageInput):
    sent_at: datetime

class User_Create_and_Login_Input(BaseModel):
    username: str
    password: str
