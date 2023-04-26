from django.db import models



class UsefulInfo(models.Model):
    name = models.CharField(max_length=255)
    info = models.TextField(blank=True)
