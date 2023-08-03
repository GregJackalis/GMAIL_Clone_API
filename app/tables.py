from pydantic import BaseModel
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text

from .database import Base

class Message(Base):
    __tablename__ = "Inbox"

    id = Column(Integer, primary_key=True, nullable=False)
    username = Column(String, nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    sent_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text
                     ('NOW()'))
