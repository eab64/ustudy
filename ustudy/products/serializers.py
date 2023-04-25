from rest_framework import serializers
from products.models import Product
from products.models import Category
from products.models import TestProcess
from products.models import UserAnswer
from products.models import Variant
from products.models import Question




class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class TestProcessSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestProcess
        fields = '__all__'

class UserAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAnswer
        fields = '__all__'
        
class VariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variant
        fields = '__all__'
           
class QuestionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Question
        fields = '__all__'

        
