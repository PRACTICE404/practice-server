from django.contrib import admin


class FinanceManagerAdminSite(admin.AdminSite):
    site_header = 'Finance Manager'


admin_site = FinanceManagerAdminSite(name='finance_manager')
