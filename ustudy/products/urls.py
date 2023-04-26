from django.urls import path

from products.api.v1.views.product import (
    ProductCategoryListAPIView, 
    ProductListAPIView, 
    ProductRetrieveAPIView,
)
from products.api.v1.views.category import (
    CategoryQuestionsAPIView, 
    CategoryRetrieveAPIView,
)
from products.api.v1.views.test import (
    TestFinishAPIView, 
    TestCreateAPIView, 
    UserAnswerAPIView,
)


urlpatterns = [
    path('products/', ProductListAPIView.as_view(), name='product-create'),
    path('products/<int:product_id>/', ProductRetrieveAPIView.as_view(), name='product-detail'),
    path('products/<int:product_id>/categories/', ProductCategoryListAPIView.as_view(), name='product-categories'),
    path('categories/<int:category_id>', CategoryRetrieveAPIView.as_view(), name='retrieve-category'),
    path('categories/<int:category_id>/questions/', CategoryQuestionsAPIView.as_view(), name='category-random-questions'),
    path('tests/', TestCreateAPIView.as_view(), name='tests'),
    path('tests/<int:test_id>/user-answers/', UserAnswerAPIView.as_view(), name='tests-user-answers'),
    path('tests/<int:test_id>/', TestFinishAPIView.as_view(), name='tests-finish'),
]
