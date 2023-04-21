from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from testing.models.test import Test
from testing.models.question import Question
from testing.models.answer import Answer

from testing.serializers.test_serializer import TestSerializer
from testing.serializers.answer_serializer import AnswerSerializer
from testing.serializers.question_serializer import QuestionSerializer

from django.shortcuts import get_object_or_404

class TestViewSet(viewsets.ViewSet): # TODO надо глянуть на generics
    queryset = Test.objects.all()
    serializer_class = TestSerializer

    @swagger_auto_schema(method='get', manual_parameters=[
        openapi.Parameter('category_id', openapi.IN_QUERY, description='айди категорий', type=openapi.TYPE_INTEGER),
    ])
    @action(detail=False, methods=['get'])
    def get_tests_by_category_id(self, request, pk=None):
        category_id = request.query_params.get('category_id')
        tests = Test.objects.filter(driving_category__id=category_id)
        serializer = TestSerializer(tests, many=True)
        return Response(serializer.data)
    
    @swagger_auto_schema(method='get', manual_parameters=[
        openapi.Parameter('test_id', openapi.IN_QUERY, description='айди категорий', type=openapi.TYPE_INTEGER),
    ])
    @action(detail=False, methods=['get'])
    def get_questions_and_answers_by_id(self, request, pk=None):
        test_id = request.query_params.get('test_id')
        test = get_object_or_404(Test, id=test_id)
        questions = test.questions.all()
        answer_serializer = AnswerSerializer
        data = []
        for question in questions:
            answers = [
                [answer_serializer(answer).data for answer in question.answers.all()]
            ]
            # answers = [{
            #     'id': answer.id,
            #     'text': answer.text,
            #     'is_correct': answer.is_correct} for answer in question.answers.all()]
            data.append(
                {"question":QuestionSerializer(question).data,
                 "answers":answers
                 }
            )
            # data.append({
            #     'id': question.id,
            #     'text': question.text,
            #     'is_multiple_choice': question.is_multiple_choice,
            #     'image':question.image if question.image else None,
            #     'answers': answers,
            # })
        return Response(data)