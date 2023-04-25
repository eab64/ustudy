from rest_framework import serializers

from tests.models.test import Test


class TestSerializer(serializers.ModelSerializer):

    class Meta:
        model = Test
        fields = ['id', 'name_ru', 'description_ru', 'name_kz', 'description_kz', 'driving_category', 'time_to_pass', 'max_errors', 'questions_count']