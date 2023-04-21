from django.db import models

from .test import Test


class Question(models.Model):
    text = models.TextField()
    is_multiple_choice = models.BooleanField(default=False)
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='questions')
    image = models.ImageField(upload_to='question_images/', blank=True, null=True)

    def __str__(self):
        return self.text