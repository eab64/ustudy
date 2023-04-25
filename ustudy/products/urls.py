from django.urls import path
# from accounts.views import UserViewSet
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
# from tests.urls import schema_view



from django.urls import include, path
from rest_framework import routers
# from products.views import ProductViewSet
# from products.views import TestProcessViewSet


# router = routers.DefaultRouter()
# router.register(r'products', ProductViewSet, basename='products')
# router.register(r'test-processes', TestProcessViewSet, basename='test-processes')
from django.urls import path
from products.views import ProductListApiView,\
    ProductRetrieveApiView, ProductCategoryListView, \
        TestCreateApiView, UserAnswerApiView, \
            CategoryQuestionsApiView, TestFinishApiView,\
                CategoryRetrieveApiView

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
    permission_classes=[permissions.AllowAny],)

urlpatterns = [
    path('products/', ProductListApiView.as_view(), name='product-create'),
    path('products/<int:product_id>/', ProductRetrieveApiView.as_view(), name='product-detail'),
    path('products/<int:product_id>/categories/', ProductCategoryListView.as_view(), name='product-categories'),
    path('categories/<int:category_id>', CategoryRetrieveApiView.as_view(), name='retrieve-category'),
    path('categories/<int:category_id>/questions/', CategoryQuestionsApiView.as_view(), name='category-random-questions'),
    path('tests/', TestCreateApiView.as_view(), name='tests'),
    path('tests/<int:test_id>/user-answers/', UserAnswerApiView.as_view(), name='tests'),
    path('tests/<int:test_id>/', TestFinishApiView.as_view(), name='tests'),

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

]





# urlpatterns = [
#     path('', include(router.urls)),
#     path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

# ]

