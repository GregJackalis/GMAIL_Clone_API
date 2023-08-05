from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from .. import tables, schemas
from ..database import connect_to_database

router = APIRouter()

# @router.post("/upload")
# def uploading():


# @router.get("/")
# def firstEndPoint(database: Session = Depends(connect_to_database)):
#     return {"message": "Hello World!"}

# @router.get("/inbox")
# def showInbox():
#     cursor

@router.get("/", status_code=status.HTTP_200_OK)
def show_inbox(database: Session = Depends(connect_to_database)):
    query = database.query(tables.Message).all()

    serializable_Data = [
        {
            "from": message.from_user,
            "to": message.to_user,
            "message_title": message.title,
            "content": message.content,
            "sent_at": message.sent_at
        }
        for message in query
    ]

    return serializable_Data

@router.post("/", status_code=status.HTTP_201_CREATED, response_model = schemas.getMessage)
def creating_message(message: schemas.sendMessageInput, database: Session = Depends(connect_to_database)):
    new_message = tables.Message(**message.dict())
    
    database.add(new_message)
    database.commit()

    database.refresh(new_message)

    return new_message