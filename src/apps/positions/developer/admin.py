from django.contrib import admin


class DeveloperAdminSite(admin.AdminSite):
    site_header = 'General Manager'


admin_site = DeveloperAdminSite(name='developer')
