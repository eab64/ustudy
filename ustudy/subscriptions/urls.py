from django.urls import path, include
from rest_framework import routers
from .views import SubscriptionViewSet
from tests.urls import schema_view
router = routers.DefaultRouter()
router.register('subscriptions', SubscriptionViewSet, basename='subscriptions')

urlpatterns = [
    path('subscriptions/', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

]