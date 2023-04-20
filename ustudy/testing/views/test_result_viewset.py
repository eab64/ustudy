from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


from datetime import datetime


from testing.models.test import Test
from testing.models.test_result import TestResult
from testing.models.user_answer import UserAnswer
from testing.models.answer import Answer
from testing.models.question import Question


from testing.serializers.test_result_serializer import TestResultSerializer

class TestResultViewSet(viewsets.ViewSet):
    
    
    @action(detail=True, methods=['get'])
    def start_test_process(self, request, pk=None):
        test = Test.objects.get(id=pk)
        user_test_result = TestResult.objects.create(test=test, user=request.user)
        serializer = TestResultSerializer(user_test_result)
        return Response(serializer.data)
    
    @swagger_auto_schema(
    method='post',
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=['question', 'answer'],
        properties={
            'question_id': openapi.Schema(type=openapi.TYPE_INTEGER),
            'answer_id': openapi.Schema(type=openapi.TYPE_INTEGER),
            'test_result_id': openapi.Schema(type=openapi.TYPE_INTEGER),
        },
    ),
)
    @action(detail=False, methods=['post'])
    def save_answer(self, request):
        test_result_id = request.data.get('test_result_id')
        user_test_result = TestResult.objects.get(id=test_result_id)
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
    
    @action(detail=True, methods=['get'])
    def finish_test(self, request, pk=None):
        user_test_result = TestResult.objects.get(id=pk)
        user_test_result.last_question_closed = datetime.now()
        user_test_result.finished = True
        user_test_result.save()
        
        data = {'балл': user_test_result.score,
                'допустимое количество ошибок': user_test_result.test.max_errors,
                'количество вопросов':user_test_result.test.questions_count
                }
        return Response(data)

    @swagger_auto_schema(method='get', manual_parameters=[
    openapi.Parameter('user_id', openapi.IN_QUERY, description='ID of the category', type=openapi.TYPE_INTEGER),
    ])
    @action(detail=False, methods=['get'])
    def get_passed_tests_result(self, request, pk=None):
        user_id = request.query_params.get('user_id')
        user_passed_tests = TestResult.objects.filter(user__id = user_id)
        user_passed_tests = TestResultSerializer(user_passed_tests, many=True)
        return Response({"Пройднные тесты пользователя":user_passed_tests.data})