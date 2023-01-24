from django.conf import settings
from django.contrib.auth.hashers import make_password
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import User, Transaction, Currency, Category
from .serializers import UserSerializer, TransactionSerializer, CurrencySerializer, CategorySerializer
from django_filters.rest_framework import DjangoFilterBackend




class UserViewSet(viewsets.ModelViewSet):
    lookup_field = "username"
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["username", "password",]

    @action(detail=True, methods=["POST"], url_path="authenticate", url_name="authenticate")
    def authenticate_user(self, request, username: str = None):
        user = self.get_object()
        password = request.data.get("password")
        if password and password == user.password:
            return Response(self.serializer_class(user).data)

        return Response({"detail": "Not found."}, status=404)


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class CurrencyViewSet(viewsets.ModelViewSet):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["is_earning"]
