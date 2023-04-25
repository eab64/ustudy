from django.db import models

from .driving_category import DrivingCategory


class Test(models.Model):
    name_ru = models.CharField(max_length=255, null=True, blank=True)
    name_kz = models.CharField(max_length=255, null=True, blank=True)
    description_ru = models.TextField(blank=True, null=True)
    description_kz = models.TextField(blank=True, null=True)
    driving_category = models.ForeignKey(DrivingCategory, on_delete=models.CASCADE, related_name='tests')
    time_to_pass = models.PositiveSmallIntegerField(default=30)
    max_errors = models.PositiveSmallIntegerField(default=3)
    questions_count = models.PositiveSmallIntegerField(default=30)

    def __str__(self):
        return self.name_ru