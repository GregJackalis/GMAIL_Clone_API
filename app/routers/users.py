from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from .. import tables, schemas
from ..database import connect_to_database

router = APIRouter()

@router.post("/create_User", status_code=status.HTTP_201_CREATED)
def create_user(input: schemas.UserCreate, database: Session = Depends(connect_to_database)):
    new_user = tables.User(**input.dict())

    database.add(new_user)
    database.commit()

    database.refresh(new_user)

    return {"new user's info" : new_user}