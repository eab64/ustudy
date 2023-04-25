from datetime import datetime
from rest_framework.generics import GenericAPIView

from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from rest_framework import viewsets
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from rest_framework import status 

from products.models import Subscription
from products.models import UsefulInfo
from products.models import Product
from products.models import Category
from products.models import Question
from products.models import Variant
from products.models import TestProcess
from products.models import UserAnswer



from products.serializers import ProductSerializer
from products.serializers import CategorySerializer
from products.serializers import TestProcessSerializer
from products.serializers import UserAnswerSerializer
from products.serializers import QuestionSerializer
from products.serializers import VariantSerializer


from accounts.models import User

from rest_framework import generics, mixins
from .serializers import ProductSerializer, CategorySerializer
from .models import Product


from drf_yasg.utils import swagger_auto_schema

class ProductListApiView(generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

class ProductRetrieveApiView(generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        product = Product.objects.get(pk=self.kwargs['product_id'])
        serializer = ProductSerializer(product)
        return Response(serializer.data)

class ProductCategoryListView(generics.GenericAPIView):
    serializer_class = CategorySerializer

    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer_class()
        product = Product.objects.get(pk=self.kwargs['product_id'])
        categories = product.categories.all()
        ser_data = serializer(categories, many=True).data
        return Response(ser_data)


class CategoryRetrieveApiView(generics.GenericAPIView):
    serializer_class = CategorySerializer

    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer_class()
        categories = Category.objects.get(pk=self.kwargs['category_id'])
        ser_data = serializer(categories).data
        return Response(ser_data)


class TestCreateApiView(generics.GenericAPIView):
    """Создать тест"""
    serializer_class = TestProcessSerializer
    
    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=['language', 'category_id'],
        properties={
            'language': openapi.Schema(type=openapi.TYPE_STRING),
            'category_id': openapi.Schema(type=openapi.TYPE_INTEGER),
        }
    ),)
    def post(self, request, *args, **kwargs):
        # language = request.data.get('language')
        category_id = request.data.get('category_id')
        user = User.objects.first()
        category = Category.objects.get(id=category_id)
        user_test_process = TestProcess.objects.create(user=user, category=category)
        return Response({"test_id":user_test_process.id})
        random_questions = category.prepare_random_questions(language=language)
        answer_serializer = VariantSerializer
        data = []
        for question in random_questions:
            answers = [answer_serializer(answer).data for answer in question.answers.all()]

            data.append(
                {"question":QuestionSerializer(question).data,
                 "answers":answers
                 }
            )
        return Response({"test_process_id":user_test_process.id,
                         "question_and_answers": data})


class TestFinishApiView(generics.GenericAPIView):
    """Завершает тест и возвращает результаты"""
    # serializer_class = TestProcessSerializer

    @swagger_auto_schema(
        query_serializer=None,
        responses={200: 'Success'}
    )
    def put(self, request, *args, **kwargs):

        test_id = self.kwargs['test_id']
        test = TestProcess.objects.get(id=test_id)
        test.finished_at = datetime.now()
        test.save()
        data = {'балл': test.score,
                'допустимое количество ошибок': test.category.max_errors,
                'количество вопросов':test.category.questions_count,
                'успешно прошел':True if test.category.questions_count - test.score < test.category.max_errors else False
                }
        return Response(status=200, data={'data': data})



class UserAnswerApiView(generics.GenericAPIView):
    @swagger_auto_schema(request_body=openapi.Schema(
        type='object',
        required=['language', 'category_id'],
        properties={
            'question_id': openapi.Schema(type='integer', description='id вопроса'),
            'variant_id': openapi.Schema(type='integer', description='id выбранного варианта'),
        }
    ))
    def post(self, request, *args, **kwargs):
        """
        Сохраняет ответы юзера в Тест
        """
        question_id = request.data.get('question_id')
        variant_id = request.data.get('variant_id')
        test_id = self.kwargs['test_id']
        if question_id and variant_id:
            UserAnswer.objects.create(
                question = Question.objects.get(id=question_id),
                answer = Variant.objects.get(id=variant_id),
                test_process_id = test_id,
                )
            return Response(status=200, data={'message': 'Ответ сохранен успешно'})
        else:
            return Response(status=400, data={'message': 'Необходимо указать question_id и answer_text'})


class CategoryQuestionsApiView(generics.GenericAPIView):
    serializer_class = CategorySerializer

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name="language",
                in_=openapi.IN_QUERY,
                description="The language of the questions to be returned",
                type=openapi.TYPE_STRING,
                required=False
            )
        ]
    )
    def get(self, request, *args, **kwargs):
        """
        Возвращает рандомное количество вопросов для категорий
        """
        language = request.query_params.get('language', 'ru')
        category_id = self.kwargs['category_id']
        category = Category.objects.get(id=category_id)

        random_questions = category.prepare_random_questions(language=language)
        answer_serializer = VariantSerializer
        data = []
        for question in random_questions:
            answers = [answer_serializer(answer).data for answer in question.answers.all()]

            data.append(
                {"question":QuestionSerializer(question).data,
                "variants":answers
                }
            )
        return Response({"questions_and_variants": data})


