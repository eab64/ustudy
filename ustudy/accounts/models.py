from django.db import models

from django.contrib.auth.models import AbstractUser


class City(models.Model):
    name = models.CharField(max_length=55)



class User(AbstractUser):
    # FIXME есть ли смысл связать его с категорией или оставить на выбор всегда
    # driving_category = models.ForeignKey(DrivingCategory, on_delete=models.SET_NULL, null=True, blank=True)
    USER_TYPE_CHOICES = [
        ('natural', 'Natural'),# физическое лицо или юридическое
        ('legal', 'Legal')
    ]
    
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES, default="natural")
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True, default=None)
    iin = models.CharField(max_length=12)
    
    def __str__(self):
        return self.username