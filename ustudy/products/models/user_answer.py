from django.db import models

from products.models.question import Question
from products.models.variant import Variant
from products.models.test import Test


class UserAnswer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Variant, on_delete=models.CASCADE)
    test_process = models.ForeignKey(Test, on_delete=models.CASCADE, related_name="user_answers")