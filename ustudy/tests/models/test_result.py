from django.db import models

from .test import Test
from accounts.models import User

class TestResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    first_question_showed = models.DateTimeField(auto_now_add=True)
    last_question_closed = models.DateTimeField(null=True)
    finished=models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.user.username} - {self.test.name}"

    def time_spend(self):
        if self.last_question_closed:
            return self.first_question_showed - self.last_question_closed
        
    @property
    def score(self):
        score = 0
        user_answers = self.user_answers.all()
        for user_answer in user_answers:
            if user_answer.answer.is_correct:
                score +=1
        return score
    
                