from sqlalchemy import Column, ForeignKey, Integer, String, Float, DateTime
from sqlalchemy.orm import relationship

from datetime import datetime

from .db import Base

class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, unique=True, index=True)
    question = Column(String)
    answer = Column(String)
    created_at = Column(DateTime)
    saved_at = Column(DateTime)