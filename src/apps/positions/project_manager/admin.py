from django.contrib import admin


class ProjectManagerAdminSite(admin.AdminSite):
    site_header = 'Project Manager'


admin_site = ProjectManagerAdminSite(name='project_manager')
