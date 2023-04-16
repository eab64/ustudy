from django.contrib import admin

# Register your models here.
from .models import Test, Question, Answer, DrivingCategory, User, UserTestResult

admin.site.register(Test)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(DrivingCategory)
admin.site.register(User)
admin.site.register(UserTestResult)