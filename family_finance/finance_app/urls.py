from django.urls import path, include
from finance_app.views import UserViewSet, TransactionViewSet, CurrencyViewSet, CategoryViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', UserViewSet, basename="user")
router.register(r'transactions', TransactionViewSet, basename="transaction")
router.register(r'currencies',  CurrencyViewSet, basename="currency")
router.register(r'categories',  CategoryViewSet, basename="category")

urlpatterns = [
    path("", include(router.urls)),
]
