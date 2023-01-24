from rest_framework import serializers
from rest_framework.response import Response
from .models import User, Category, Transaction, Currency


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ["id", "username", "password", "categories"]


class TransactionSerializer(serializers.ModelSerializer):
    category_title = serializers.CharField(source="category.title", read_only=True)
    currency_short = serializers.CharField(source="currency.short_name", read_only=True)

    class Meta:
        model = Transaction
        fields = ["id", "category", "currency", "amount", "user", "category_title", "currency_short"]

class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ["id", "short_name"]

