from django.contrib.auth.models import AbstractUser
from django.db import models


class DrivingCategory(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class User(AbstractUser):
    driving_category = models.ForeignKey(DrivingCategory, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.username


class Test(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    driving_category = models.ForeignKey(DrivingCategory, on_delete=models.CASCADE, related_name='tests')
    time_to_pass = models.PositiveSmallIntegerField(default=30)
    max_errors = models.PositiveSmallIntegerField(default=3)
    questions_count = models.PositiveSmallIntegerField(default=30)

    def __str__(self):
        return self.name

class Question(models.Model):
    text = models.TextField()
    is_multiple_choice = models.BooleanField(default=False)
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='questions')

    def __str__(self):
        return self.text


class Answer(models.Model):
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')

    def __str__(self):
        return self.text


class UserTestResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    first_question_showed = models.DateTimeField(auto_now_add=True)
    last_question_closed = models.DateTimeField(null=True)
    finished=models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.user.username} - {self.test.name}"

    @property
    def score(self):
        score = 0
        user_answers = self.user_answers.all()
        for user_answer in user_answers:
            if user_answer.answer.is_correct:
                score +=1
        return score
                


class UserAnswer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    test_result = models.ForeignKey(UserTestResult, on_delete=models.CASCADE, related_name="user_answers")

    