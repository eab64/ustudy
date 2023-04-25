from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from tests.models.test import Test
from tests.models.question import Question
from tests.models.answer import Answer

from tests.serializers.test_serializer import TestSerializer
from tests.serializers.answer_serializer import AnswerSerializer
from tests.serializers.question_serializer import QuestionSerializer

from django.shortcuts import get_object_or_404

class TestViewSet(viewsets.ReadOnlyModelViewSet): # TODO надо глянуть на generics
    queryset = Test.objects.all()
    serializer_class = TestSerializer

    
    @swagger_auto_schema(method='get', manual_parameters=[
        openapi.Parameter('language', openapi.IN_QUERY, description='язык', type=openapi.TYPE_STRING),
    ])
    @action(detail=True, methods=['get'], url_path='questions_and_answers')
    def get_questions_and_answers_by_id(self, request, pk=None):
        language = request.query_params.get('language')
        test = Test.objects.get(id=pk)

        questions = test.questions.filter(language=language)
        answer_serializer = AnswerSerializer
        data = []
        for question in questions:
            answers = [answer_serializer(answer).data for answer in question.answers.all()]

            data.append(
                {"question":QuestionSerializer(question).data,
                 "answers":answers
                 }
            )

        return Response(data)