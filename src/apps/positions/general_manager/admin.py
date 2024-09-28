from django.contrib import admin


class GeneralManagerAdminSite(admin.AdminSite):
    site_header = 'General Manager'


admin_site = GeneralManagerAdminSite(name='general_manager')
