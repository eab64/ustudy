from datetime import datetime

from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from accounts.models import User
from products.models.user_answer import UserAnswer
from products.models.test import Test
from products.models.category import Category
from products.models.question import Question
from products.models.variant import Variant

from products.api.v1.serializers.test_serializers import TestSerializer


class TestCreateAPIView(GenericAPIView):
    """
    Создать тест
    """
    serializer_class = TestSerializer

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['language', 'category_id'],
            properties={
                'language': openapi.Schema(type=openapi.TYPE_STRING), #TODO чекнуть и удалить
                'category_id': openapi.Schema(type=openapi.TYPE_INTEGER),
            }
        )
    )
    def post(self, request, *args, **kwargs):
        category_id = request.data.get('category_id')
        user = User.objects.first()
        category = Category.objects.get(id=category_id)
        user_test_process = Test.objects.create(user=user, category=category)
        return Response({"test_id": user_test_process.id})


class TestFinishAPIView(GenericAPIView):
    """
    Completes the test and returns the results
    """
    @swagger_auto_schema(
        query_serializer=None,
        responses={200: 'Success'}
    )
    def put(self, request, *args, **kwargs):
        test_id = self.kwargs['test_id']
        test = Test.objects.get(id=test_id)
        test.finished_at = datetime.now()
        test.save()
        data = {
            'балл': test.score,
            'допустимое количество ошибок': test.category.max_errors,
            'количество вопросов': test.category.questions_count,
            'успешно прошел': True if test.category.questions_count - test.score < test.category.max_errors else False
        }
        return Response(status=200, data={'data': data})


class UserAnswerAPIView(GenericAPIView):
    """
    Saves user answers in the Test
    """
    @swagger_auto_schema(
        request_body=openapi.Schema(
            type='object',
            required=['language', 'category_id'],
            properties={
                'question_id': openapi.Schema(type='integer', description='id вопроса'),
                'variant_id': openapi.Schema(type='integer', description='id выбранного варианта'),
            }
        )
    )
    def post(self, request, *args, **kwargs):
        question_id = request.data.get('question_id')
        variant_id = request.data.get('variant_id')
        test_id = self.kwargs['test_id']
        
        if question_id and variant_id:
            UserAnswer.objects.create(
                question=Question.objects.get(id=question_id),
                answer=Variant.objects.get(id=variant_id),
                test_process_id=test_id,
            )
            return Response(status=200, data={'message': 'Ответ сохранен успешно'})
        else:
            return Response(status=400, data={'message': 'Необходимо указать question_id и variant_id'})

