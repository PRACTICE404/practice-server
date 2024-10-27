from django.contrib import admin


class BusinessAnalystAdminSite(admin.AdminSite):
    site_header = 'Salesman'


admin_site = BusinessAnalystAdminSite(name='salesman')
