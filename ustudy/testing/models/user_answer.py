from django.db import models

from accounts.models import User
from .question import Question
from .answer import Answer
from .test_result import TestResult

class UserAnswer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    test_result = models.ForeignKey(TestResult, on_delete=models.CASCADE, related_name="user_answers")