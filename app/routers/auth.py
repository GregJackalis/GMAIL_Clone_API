from fastapi import APIRouter, Depends, status, HTTPException, Response
from sqlalchemy.orm import Session
from .. import database, tables, utils
from fastapi.security.oauth2 import OAuth2PasswordRequestForm

router = APIRouter()

@router.post("/login")
def login(input: OAuth2PasswordRequestForm = Depends(), database : Session = Depends(database.connect_to_database)):
    
    #sql code with sqlachemy: checking if there is a user in the database same with the given username 
    user = database.query(tables.User).filter(input.username == tables.User.username).first

    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Login Credentials")
    if not utils.verify_password(input.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Password")
    