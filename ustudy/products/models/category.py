from django.db import models
import random

from .product import Product


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