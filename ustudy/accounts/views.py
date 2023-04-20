from rest_framework import viewsets
from rest_framework.response import Response

from accounts.models import User
from accounts.serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'  # or any other field you want to use for lookup

    http_method_names = ['get', 'put']

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', True)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save()

    def get_allowed_actions(self):
        allowed_actions = []
        for method in self.http_method_names:
            if method == 'get':
                allowed_actions.append('retrieve')
            elif method == 'put':
                allowed_actions.append('update')
        return allowed_actions
