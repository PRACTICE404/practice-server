from django.contrib import admin


class DeveloperAdminSite(admin.AdminSite):
    site_header = 'Developer'


admin_site = DeveloperAdminSite(name='developer')
