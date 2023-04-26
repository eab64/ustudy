from rest_framework.generics import GenericAPIView

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from rest_framework.response import Response

from products.api.v1.serializers.category_serializers import CategorySerializer
from products.api.v1.serializers.question_serializers import QuestionSerializer
from products.api.v1.serializers.variant_serializers import VariantSerializer


from products.models.category import Category


class CategoryRetrieveAPIView(GenericAPIView):
    serializer_class = CategorySerializer

    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer_class()
        categories = Category.objects.get(pk=self.kwargs['category_id'])
        ser_data = serializer(categories).data
        return Response(ser_data)


class CategoryQuestionsAPIView(GenericAPIView):
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
