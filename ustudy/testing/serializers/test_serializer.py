from rest_framework import serializers

from testing.models.test import Test


class TestSerializer(serializers.ModelSerializer):

    class Meta:
        model = Test
        fields = ['id', 'name', 'description', 'driving_category', 'time_to_pass', 'max_errors']