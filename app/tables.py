from pydantic import BaseModel
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text

from .database import Base

class Message(Base):
    __tablename__ = "Inbox"

    id = Column(Integer, primary_key=True, nullable=False)
    from_user = Column(String, nullable=False)
    to_user = Column(String, nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    sent_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text
                     ('NOW()'))
    

class User(Base):
    __tablename__ = "Users"

    id = Column(Integer, nullable= False, primary_key=True)
    username = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
