from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import permissions

from snippets.permissions import IsOwnerOrReadOnly
from snippets.serializers import UserSerializer


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)


def perform_create(self, serializer):
    serializer.save(owner=self.request.user)
