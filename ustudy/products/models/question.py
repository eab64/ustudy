from django.db import models

from .category import Category

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