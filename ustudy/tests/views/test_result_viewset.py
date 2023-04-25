from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


from datetime import datetime


from tests.models.test import Test
from tests.models.test_result import TestResult
from tests.models.user_answer import UserAnswer
from tests.models.answer import Answer
from tests.models.question import Question

from tests.serializers.test_result_serializer import TestResultSerializer

from accounts.models import User

class TestResultViewSet(viewsets.ViewSet):
    
    
    @swagger_auto_schema(method='post', manual_parameters=[
        openapi.Parameter('test_id', openapi.IN_QUERY, description='id теста', type=openapi.TYPE_INTEGER),
    ])
    @action(detail=False, methods=['post'])
    def start_test_process(self, request, pk=None):
        test_id = request.query_params.get('test_id')
        test = Test.objects.get(id=test_id)
        user = User.objects.first()
        user_test_result = TestResult.objects.create(test=test, user=user)

        # user_test_result = TestResult.objects.create(test=test, user=request.user)
        serializer = TestResultSerializer(user_test_result)
        return Response(serializer.data)
    
    @swagger_auto_schema(method='post', manual_parameters=[
        openapi.Parameter('question_id', openapi.IN_QUERY, description='id вопроса', type=openapi.TYPE_INTEGER),
        openapi.Parameter('answer_id', openapi.IN_QUERY, description='id выбранного ответа', type=openapi.TYPE_INTEGER),
    ])
    @action(detail=True, methods=['post'])
    def save_answer(self, request, pk=None):
        user_test_result = TestResult.objects.get(id=pk)
        question_id = request.data.get('question_id')
        answer_id = request.data.get('answer_id')
        if question_id and answer_id:
            UserAnswer.objects.create(
                question = Question.objects.get(id=question_id),
                answer = Answer.objects.get(id=answer_id),
                test_result = user_test_result,
                )
            return Response(status=200, data={'message': 'Ответ сохранен успешно'})
        else:
            return Response(status=400, data={'message': 'Необходимо указать question_id и answer_text'})
    
    @swagger_auto_schema(method='post', manual_parameters=[
        openapi.Parameter('test_process_id', openapi.IN_QUERY, description='id процесса тестирования', type=openapi.TYPE_INTEGER),
    ])
    @action(detail=True, methods=['post'])
    def finish_test_process(self, request, pk=None):
        test_process_id = request.query_params.get('test_process_id')
        user_test_result = TestResult.objects.get(id=test_process_id)
        user_test_result.last_question_closed = datetime.now()
        user_test_result.finished = True
        user_test_result.save()
        
        data = {'балл': user_test_result.score,
                'допустимое количество ошибок': user_test_result.test.max_errors,
                'количество вопросов':user_test_result.test.questions_count,
                'успешно прошел':True if user_test_result.test.questions_count - user_test_result.score < user_test_result.test.max_errors else False
                }
        return Response(data)

    @swagger_auto_schema(method='get', manual_parameters=[
    openapi.Parameter('user_id', openapi.IN_QUERY, description='ID of the category', type=openapi.TYPE_INTEGER),
    ])
    @action(detail=False, methods=['get'], url_path='user_results')
    def get_user_results(self, request, pk=None):
        user_id = request.query_params.get('user_id')
        user_passed_tests = TestResult.objects.filter(user__id = user_id)
        user_passed_tests = TestResultSerializer(user_passed_tests, many=True)
        return Response({"Пройднные тесты пользователя":user_passed_tests.data})