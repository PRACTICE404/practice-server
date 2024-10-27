from django.contrib import admin

from apps.projects.admin import ProjectAdmin
from apps.projects.models import Project

from apps.orders.admin import (
    OrderAdmin,
    EpicAdmin,
    TaskAdmin
)
from apps.orders.models import (
    Order,
    Epic,
    Task
)

from apps.sessions_.admin import SessionAdmin
from apps.sessions_.models import Session


class DeveloperAdminSite(admin.AdminSite):
    site_header = 'Developer'


admin_site = DeveloperAdminSite(name='developer')


@admin.register(Project, site=admin_site)
class ProjectAdminForDeveloper(ProjectAdmin):
    autocomplete_fields = ()
    exclude = ('customer',)


@admin.register(Order, site=admin_site)
class OrderAdminForDeveloper(OrderAdmin):
    pass


@admin.register(Epic, site=admin_site)
class EpicAdminForDeveloper(EpicAdmin):
    pass


@admin.register(Task, site=admin_site)
class TaskAdminForDeveloper(TaskAdmin):
    pass


@admin.register(Session, site=admin_site)
class SessionAdminForDeveloper(SessionAdmin):
    pass
