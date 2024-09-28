from django.contrib import admin


class MarketerAdminSite(admin.AdminSite):
    site_header = 'Marketer'


admin_site = MarketerAdminSite(name='marketer')
