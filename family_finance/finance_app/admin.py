from django.contrib import admin

from .models import User, Category, Currency, Transaction


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["username",]
    # list_filter = ["is earnings",]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_filter = ["is_earning"]
    list_display = ["title", "is_earning"]


@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ["short_name", "created_at"]

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    pass