
from rest_framework import serializers


from products.models.user_answer import UserAnswer



class UserAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAnswer
        fields = '__all__'