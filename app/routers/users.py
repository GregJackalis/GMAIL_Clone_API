from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from .. import tables, schemas
from ..database import connect_to_database

router = APIRouter()

@router.post("/create_User", status_code=status.HTTP_201_CREATED)
def create_user(input: schemas.UserCreateInput, database: Session = Depends(connect_to_database)):
    new_user = tables.User(**input.dict())

    database.add(new_user)
    database.commit()

    database.refresh(new_user)


    ##SINCE I haven't fixed the response model problem, I'm returning the user's info without the password like this
    return {"user was created": f"""username: {new_user.username},
            id: {new_user.id}"""}