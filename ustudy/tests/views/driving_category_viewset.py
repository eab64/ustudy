

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from tests.models.driving_category import DrivingCategory
from tests.models.test import Test
from tests.serializers.driving_category_serializer import DrivingCategorySerializer
from tests.serializers.test_serializer import TestSerializer

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from rest_framework.permissions import AllowAny


class DrivingCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows driving categories to be viewed.
    """
    # permission_classes = [AllowAny]
    queryset = DrivingCategory.objects.all()
    serializer_class = DrivingCategorySerializer

    @action(detail=True, methods=['get'],  url_path='tests')
    def get_tests(self, request, pk=None):
        category_id = pk
        tests = Test.objects.filter(driving_category__id=category_id)
        serializer = TestSerializer(tests, many=True)
        return Response(serializer.data)
