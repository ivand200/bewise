from fastapi import FastAPI, Depends, Response
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from starlette import status

import requests
import json
from datetime import datetime
import logging
import sys

from database import models, schemas
from database.db import engine, get_db

models.Base.metadata.create_all(bind=engine)

logger = logging.getLogger()
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.INFO)
handler_format = logging.Formatter("%(asctime)s-%(message)s")
handler.setFormatter(handler_format)
logger.addHandler(handler)

app = FastAPI()


@app.get("/")
async def home():
    return "Hello World"


@app.post("/question/{questions}", response_model=schemas.QuestionBase, status_code=201)
async def get_question(questions: int, db: Session = Depends(get_db)):
    """
    Get required numbers of questions
    """

    def check_question(id):
        check_question = (
            db.query(models.Question).filter(models.Question.id == id).first()
        )
        return check_question

    list_of_questions = requests.get(
        f"https://jservice.io/api/random?count={questions}"
    ).json()
    for question in list_of_questions:
        if check_question(question["id"]):
            continue
        logger.info(f"Added question: {question['id']}")
        question_db = models.Question(
            id=question["id"],
            question=question["question"],
            answer=question["answer"],
            created_at=question["created_at"],
            saved_at=datetime.now())
        db.add(question_db)
        print(question_db.id)
    db.commit()
    try:
        question_response = (
            db.query(models.Question).order_by(models.Question.saved_at.desc()).all()
        )
        serializer_question = schemas.QuestionBase(
            id=question_response[questions].id,
            question=question_response[questions].question,
            answer=question_response[questions].answer,
            created_at=question_response[questions].created_at
        )
    except:
        serializer_question = schemas.QuestionBase()
    return serializer_question

