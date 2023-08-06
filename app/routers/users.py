from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from .. import tables, schemas, utils
from ..database import connect_to_database

router = APIRouter()

@router.post("/create_User", status_code=status.HTTP_201_CREATED)
def create_user(input: schemas.UserCreateInput, database: Session = Depends(connect_to_database)):

    #hash the given password first
    hashed_password = utils.hash_password(input.password)

    #we replace the password given with the hashed password
    input.password = hashed_password

    #we make a variable that makes a dictionary out of the input and based on the User class' columns, in tables.py
    new_user = tables.User(**input.dict())

    #we add the variable to the database
    database.add(new_user)
    database.commit()

    database.refresh(new_user)


    ##SINCE I haven't fixed the response model problem, I'm returning the user's info without the password like this
    return new_user