from django.db import models


from products.models.category import Category
from accounts.models import User



class Test(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    started_at = models.DateTimeField(auto_now_add=True)
    finished_at = models.DateTimeField(null=True)
    finished=models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.user.username} - {self.test.name}"