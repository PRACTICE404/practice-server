from django.contrib import admin


class BusinessAnalystAdminSite(admin.AdminSite):
    site_header = 'Business Analyst'


admin_site = BusinessAnalystAdminSite(name='business_analyst')
