from django.db import models
import random



class UsefulInfo(models.Model):
    name = models.CharField(max_length=255)
    info = models.TextField(blank=True)


class Subscription(models.Model):
    active_until = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    
    def __str__(self) -> str:
        return self.price

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE)
    useful_info = models.ForeignKey(UsefulInfo, null=True, blank=True, on_delete=models.SET_NULL)
    paid = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    description_ru = models.TextField(blank=True, null=True)
    description_kz = models.TextField(blank=True, null=True)
    time_to_pass = models.PositiveSmallIntegerField(default=30)
    max_errors = models.PositiveSmallIntegerField(default=3)
    questions_count = models.PositiveSmallIntegerField(default=30)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="categories")
    
    def prepare_random_questions(self, language: str):
        questions = list(self.questions.filter(language=language))
        if len(questions) < self.questions_count:
            raise ValueError(f"Not enough questions in category {self.name} for language {language}")
        random.shuffle(questions)
        return questions[:self.questions_count]
        
    def __str__(self) -> str:
        return self.name
    
class Question(models.Model):
    text = models.TextField()
    is_multiple_choice = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='questions')
    image = models.ImageField(upload_to='question_images/', blank=True, null=True)
    LANGUAGE_CHOICES = [
        ('kz', 'Kz'),
        ('ru', 'Ru')
    ]
    language = models.CharField(max_length=20, choices=LANGUAGE_CHOICES, default="ru")
    
    def __str__(self):
        return self.text
    

class Variant(models.Model):
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')

    def __str__(self):
        return self.text
    
from accounts.models import User

class TestProcess(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    started_at = models.DateTimeField(auto_now_add=True)
    finished_at = models.DateTimeField(null=True)
    finished=models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.user.username} - {self.test.name}"

        
    @property
    def score(self):
        # score = 0
        correct_answers = self.user_answers.filter(answer__is_correct=True).count()
        return correct_answers
        # for user_answer in user_answers:
        #     if user_answer.answer.is_correct:
        #         score +=1
        # return score
    
    
class UserAnswer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Variant, on_delete=models.CASCADE)
    test_process = models.ForeignKey(TestProcess, on_delete=models.CASCADE, related_name="user_answers")
    
    