from rest_framework import serializers

from tests.models.driving_category import DrivingCategory

class DrivingCategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = DrivingCategory
        fields = ['id', 'name', 'description']