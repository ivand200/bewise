from datetime import datetime
from typing import Optional
from datetime import datetime

from pydantic import BaseModel

class QuestionBase(BaseModel):
    id: Optional[int]
    question: Optional[str]
    answer: Optional[str]
    created_at: Optional[datetime]

    class Config:
        orm_mode = True
