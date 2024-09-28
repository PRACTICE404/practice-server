from django.core.exceptions import ValidationError
from django.db import models

from apps.base.models import Record
from apps.orders.models import Order


class Currency(Record):
    name = models.CharField(max_length=24)
    code = models.CharField(max_length=8)

    def __str__(self):
        return f"{self.code} ({self.name})"

    class Meta:
        verbose_name_plural = '(C) Currencies'


class Account(Record):
    name = models.CharField(max_length=48)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.currency.code})"

    class Meta:
        verbose_name_plural = '(A) Accounts'


class Operation(Record):
    symbol = "+"
    value = models.PositiveIntegerField()
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.symbol}{self.value} {self.account.currency} ({self.account.name})"  # NOQA

    class Meta:
        abstract = True


class Deposit(Operation):
    symbol = "+"

    class Meta:
        verbose_name_plural = '(B.A) Deposit'


class Withdraw(Operation):
    symbol = "-"

    class Meta:
        verbose_name_plural = '(B.B) Withdraw'


class DepositDistribution(Record):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    deposit = models.ForeignKey(Deposit, on_delete=models.CASCADE, related_name='distributions')  # NOQA
    value = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.deposit} > {self.order} ({self.value})'

    def clean_fields(self, exclude=None):
        if (self.deposit.distributions.exclude(id=self.id).aggregate(models.Sum('value'))['value__sum'] or 0) + self.value > self.deposit.value:  # NOQA
            raise ValidationError({
                'value': 'More than possible is distributed!',
            })


class Swap(Record):
    account_from = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='swap_from')  # NOQA
    account_to = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='swap_to')  # NOQA
    value_from = models.PositiveIntegerField()
    value_to = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.account_from.name} ({self.value_from} {self.account_from.currency}) > {self.account_to.name} ({self.value_to} {self.account_to.currency})"  # NOQA

    class Meta:
        verbose_name_plural = '(B.C) Swap'
