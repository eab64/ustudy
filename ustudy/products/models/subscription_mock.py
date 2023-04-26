from django.db import models



class Subscription(models.Model):
    active_until = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    
    def __str__(self) -> str:
        return self.price