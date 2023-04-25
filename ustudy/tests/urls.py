from django.urls import path, include
from rest_framework import routers


from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from .views.test_viewset import TestViewSet
from .views.driving_category_viewset import DrivingCategoryViewSet
from .views.test_result_viewset import TestResultViewSet


schema_view = get_schema_view(
    openapi.Info(
        title="API",
        default_version='v1',
        description="API documentation",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@api.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


router = routers.DefaultRouter()
router.register(r'driving-categories', DrivingCategoryViewSet)
router.register(r'tests', TestViewSet)
router.register(r'test-processes', TestResultViewSet, basename='testing-process')


urlpatterns = [
    path('', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
