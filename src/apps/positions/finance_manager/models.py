from apps.payments.models import Deposit


class DepositSummaryByDays(Deposit):
    class Meta:
        proxy = True
        verbose_name_plural = ' Deposit summary (by days)'


class DepositSummaryByMonths(Deposit):
    class Meta:
        proxy = True
        verbose_name_plural = ' Deposit summary (by months)'
