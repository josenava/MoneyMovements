from api.models import Category, Transaction
from api.serializers import CategorySerializer, UserSerializer, TransactionSerializer
from rest_framework import generics, permissions, views
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from django.contrib.auth.models import User
from io import TextIOWrapper
import csv

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
    serializer_class = TransactionSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class MovementDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TransactionSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)


class BulkUpload(views.APIView):
    parser_classes = (MultiPartParser,)
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        # TODO validate and parse file
        csv_file = TextIOWrapper(request.data['file'])
        # movements = CSVParser.convert_to(file, serializer=TransactionSerializer)
        reader = csv.DictReader(csv_file)
        for row in reader:
            row['categories'] = []
            row['user'] = request.user.id
            serializer = TransactionSerializer(data=row)
            if serializer.is_valid():
                serializer.save(user=self.request.user)

        return Response()

