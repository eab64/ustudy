

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from testing.models.driving_category import DrivingCategory
from testing.serializers.driving_category_serializer import DrivingCategorySerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class DrivingCategoryViewSet(viewsets.ViewSet):
    """
    API endpoint that allows driving categories to be viewed.
    """
    queryset = DrivingCategory.objects.all()
    serializer_class = DrivingCategorySerializer

    @swagger_auto_schema(
    operation_summary="Все доступные категории",
)
    @action(detail=False, methods=["get"])
    def get_all_categories(self, request):
        """
        List all driving categories.
        """
        serializer = DrivingCategorySerializer(self.queryset, many=True)
        return Response(serializer.data)