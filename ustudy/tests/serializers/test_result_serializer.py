from rest_framework import serializers

from tests.models.test_result import TestResult
from .test_serializer import TestSerializer

class TestResultSerializer(serializers.ModelSerializer):
    test = TestSerializer()
    
    class Meta:
        model = TestResult
        fields = ['id', 'user', 'test', 'score', 'finished']