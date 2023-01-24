from django.db import models
from django.contrib.auth.models import User




class BaseDateMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class User(models.Model):

    username = models.CharField(verbose_name="Имя", max_length=255, unique=True)
    password = models.CharField(verbose_name="Пароль", max_length=255)
    # email = models.EmailField(verbose_name="Адрес электронной почты")

    def __str__(self) -> str:
        return self.username


class Category(BaseDateMixin):
    title = models.CharField(max_length=255)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='categories',
    )
    is_earning = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name_plural = "Categories"


class Transaction(BaseDateMixin):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='transactions',
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="transactions",
    )
    currency = models.ForeignKey(
        "Currency",
        on_delete=models.PROTECT,
        related_name="transactions"

    )
    is_earning = models.BooleanField(default=False)
    amount = models.DecimalField(max_digits=9, decimal_places=2)


    def __str__(self) -> str:
        return f"{self.user} | {self.amount}"

class Currency(BaseDateMixin):

      title = models.CharField(max_length=100)
      short_name = models.CharField(max_length=3)

      def __str__(self) -> str:
          return self.short_name

      class Meta:
          verbose_name_plural = "Currencies"






# currency_choices = (("USD", "USD"), ("BYN", "BYN")), ("EUR", "EUR"))
#
#
# class BalanceLessZeroError(Exception):
#     """BalanceLessZeroError."""
#
#
# class Wallet(models.Model):
#     user = models.ForeignKey(
#         User,
#         on_delete=models.PROTECT,
#         related_name="wallet",
#     )
#     currency = models.CharField(max_length=3, choices=currency_choices)
#     last_transaction_at = models.DateTimeField(null=True, blank=True)
#
#     @property
#     def balance(self):
#
#             negative = sum(obj.total for obj in self.send_transactions.all())
#             positive = sum(obj.total for obj in self.receive_transactions.all())
#             return positive - negative
#
#
#
#     def __str__(self) -> str:
#         return f"{self.user.username} | balance:{self.balance}"
#
#     def save(self, *args, **kwargs):
#         if not self.pk:
#             if self.from_wallet.balance - self.total < 0:
#                 raise BalanceLessZeroError
#         return super().save(*args, **kwargs)
#
