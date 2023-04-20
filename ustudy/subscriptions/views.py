from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.response import Response

from .models import Subscription
from .serializers import SubscriptionSerializer

class SubscriptionViewSet(viewsets.ModelViewSet):
    serializer_class = SubscriptionSerializer

    def get_queryset(self):
        return Subscription.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def activate_subscription(self, request, pk):
        subscription = self.get_object()
        subscription.is_active = True
        subscription.save()
        return Response({'status': 'success'})

    def deactivate_subscription(self, request, pk):
        subscription = self.get_object()
        subscription.is_active = False
        subscription.save()
        return Response({'status': 'success'})

