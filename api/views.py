from api.models import Category, Movement
from api.serializers import CategorySerializer, UserSerializer, MovementSerializer
from rest_framework import generics, permissions, views
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from django.contrib.auth.models import User


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)


class CategoryList(generics.ListCreateAPIView):
    serializer_class = CategorySerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)


class MovementList(generics.ListCreateAPIView):
    serializer_class = MovementSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Movement.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class MovementDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MovementSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Movement.objects.filter(user=self.request.user)


class BulkUpload(views.APIView):
    parser_classes = (MultiPartParser,)
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        # TODO validate and parse file
        file = request.data['file']
        return Response({'test': 'successful'})

