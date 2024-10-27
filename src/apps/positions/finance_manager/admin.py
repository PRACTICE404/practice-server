from django.contrib import admin

from apps.payments.admin import (
    CurrencyAdmin,
    AccountAdmin,
    DepositAdmin,
    WithdrawAdmin,
    SwapAdmin
)
from apps.payments.models import (
    Currency,
    Account,
    Deposit,
    Withdraw,
    Swap
)


class FinanceManagerAdminSite(admin.AdminSite):
    site_header = 'Finance Manager'


admin_site = FinanceManagerAdminSite(name='finance_manager')


@admin.register(Currency, site=admin_site)
class CurrencyAdminForFinanceManager(CurrencyAdmin):
    pass


@admin.register(Account, site=admin_site)
class AccountAdminForFinanceManager(AccountAdmin):
    pass


@admin.register(Deposit, site=admin_site)
class DepositAdminForFinanceManager(DepositAdmin):
    pass


@admin.register(Withdraw, site=admin_site)
class WithdrawAdminForFinanceManager(WithdrawAdmin):
    pass


@admin.register(Swap, site=admin_site)
class SwapAdminForFinanceManager(SwapAdmin):
    pass
