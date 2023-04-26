from django.db import models

from .subscription_mock import Subscription
from .useful_info import UsefulInfo


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE)
    useful_info = models.ForeignKey(UsefulInfo, null=True, blank=True, on_delete=models.SET_NULL)
    paid = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name