from rest_framework import serializers
from .models import Test, Question, Answer, DrivingCategory, UserTestResult


class DrivingCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = DrivingCategory
        fields = ['id', 'name', 'description']
        


class AnswerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Answer
        fields = ['id', 'text', 'is_correct']

class QuestionSerializer(serializers.ModelSerializer):
    answer = AnswerSerializer()
    class Meta:
        model = Question
        fields = ['id', 'text', 'is_multiple_choice', 'answer']



class TestSerializer(serializers.ModelSerializer):

    class Meta:
        model = Test
        fields = ['id', 'name', 'description', 'driving_category', 'time_to_pass', 'max_errors']


class UserTestResultSerializer(serializers.ModelSerializer):
    test = TestSerializer()
    class Meta:
        model = UserTestResult
        fields = ['id', 'user', 'test', 'score']

