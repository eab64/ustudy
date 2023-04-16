from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .models import Test, Question, Answer, UserTestResult, DrivingCategory, UserAnswer
from .serializers import (
TestSerializer, QuestionSerializer, AnswerSerializer, UserTestResultSerializer,
DrivingCategorySerializer
)

from datetime import datetime


class DrivingCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows driving categories to be viewed.
    """
    queryset = DrivingCategory.objects.all()
    serializer_class = DrivingCategorySerializer


class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer

    @action(detail=True, methods=['get'])
    def questions(self, request, pk=None):
        test = self.get_object()
        questions = test.questions.all()
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)
    
    @swagger_auto_schema(method='get', manual_parameters=[
        openapi.Parameter('category_id', openapi.IN_QUERY, description='ID of the category', type=openapi.TYPE_INTEGER),
    ])
    @action(detail=False, methods=['get'])
    def get_tests_by_category_id(self, request, pk=None):
        category_id = request.query_params.get('category_id')

        tests = Test.objects.filter(driving_category__id = category_id)
        serializer = TestSerializer(tests, many=True)
        return Response(serializer.data)
    

    


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    @action(detail=True, methods=['get'])
    def answers(self, request, pk=None):
        question = self.get_object()
        answers = question.answers.all()
        serializer = AnswerSerializer(answers, many=True)
        return Response(serializer.data)


class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    
    @action(detail=True, methods=['get'])
    def is_correct(self, request, pk=None):
        answer = self.get_object()
        return Response({'is_correct': answer.is_correct})





class TestPassingViewSet(viewsets.ViewSet):
    
    @action(detail=True, methods=['get'])
    def start_test(self, request, pk=None):
        # получаем объект теста по его идентификатору
        test = Test.objects.get(id=pk)
        user_test_result = UserTestResult.objects.create(test=test, user=request.user)
        serializer = UserTestResultSerializer(user_test_result)
        return Response(serializer.data)
    
    
    @swagger_auto_schema(
    method='post',
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=['question', 'answer'],
        properties={
            'question_id': openapi.Schema(type=openapi.TYPE_INTEGER),
            'answer_id': openapi.Schema(type=openapi.TYPE_INTEGER),
        },
    ),
)
    @action(detail=True, methods=['post'])
    def save_answer(self, request, pk=None):
        user_test_result = UserTestResult.objects.get(id=pk)
        question_id = request.data.get('question_id')
        answer_id = request.data.get('answer_id')
        if question_id and answer_id:
            UserAnswer.objects.create(
                user = user_test_result.user,
                question = Question.objects.get(id=question_id),
                answer = Answer.objects.get(id=answer_id),
                test_result = user_test_result,
                )
            return Response(status=200, data={'message': 'Ответ сохранен успешно'})
        else:
            return Response(status=400, data={'message': 'Необходимо указать question_id и answer_text'})
    
    @action(detail=True, methods=['get'])
    def finish_test(self, request, pk=None):
        user_test_result = UserTestResult.objects.get(id=pk)
        user_test_result.last_question_closed = datetime.now()
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
    def get_passed_tests_for_user(self, request, pk=None):
        user_id = request.query_params.get('user_id')
        user_passed_tests = UserTestResult.objects.filter(user__id = user_id)
        user_passed_tests = UserTestResultSerializer(user_passed_tests, many=True)
        return Response({"Пройднные тесты пользователя":user_passed_tests.data})