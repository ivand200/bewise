from database import models
from datetime import datetime

import pytest

def test_new_question():
    """
    GIVEN a Question model
    WHEN a new Question is created
    THEN check the id, question, answer
    """
    question = models.Question(
        id = 666, 
        question = "Why so serious?", 
        answer = "Because you can't put a smile on my face",
        created_at = datetime.now(),
        saved_at = datetime.now()
        )
    assert question.id == 666
    assert question.question == "Why so serious?"
    assert question.answer == "Because you can't put a smile on my face"