from import_export import resources

from products.models import Category
from products.models import Subscription
from products.models import Product
from products.models import Question
from products.models import Variant



class SubscriptionResource(resources.ModelResource):
    class Meta:
        model = Subscription
        fields = ('id', 'active_until', 'price')


class ProductResource(resources.ModelResource):
    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'subscription', 'useful_info', 'paid')


class CategoryResource(resources.ModelResource):
    class Meta:
        model = Category
        fields = ('id', 'name', 'description_ru', 'description_kz', 'time_to_pass', 'max_errors', 'questions_count', 'product')


class QuestionResource(resources.ModelResource):
    class Meta:
        model = Question
        fields = ('id', 'text', 'is_multiple_choice', 'category', 'image', 'language')


class VariantResource(resources.ModelResource):
    class Meta:
        model = Variant
        fields = ('id', 'text', 'is_correct', 'question')