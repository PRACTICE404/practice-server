from django.contrib import admin

from apps.customers.admin import CustomerAdmin
from apps.customers.models import Customer

from apps.base.admin import SummaryDailyAdmin

from apps.projects.admin import ProjectAdmin
from apps.projects.models import Project

from apps.orders.admin import (
    TaskAdmin,
    EpicAdmin,
    OrderHistoryAdmin,
    OrderAdmin
)
from apps.orders.models import (
    Task,
    Epic,
    OrderHistory,
    Order
)

from apps.sessions_.admin import SessionAdmin
from apps.sessions_.models import Session

from apps.payments.admin import DepositAdmin
from apps.payments.models import Deposit

from apps.services.admin import PortfolioAdmin
from apps.services.models import Portfolio

from . import models


class ProjectManagerAdminSite(admin.AdminSite):
    site_header = 'Project Manager'


admin_site = ProjectManagerAdminSite(name='project_manager')


@admin.register(Customer, site=admin_site)
class CustomerAdminForProjectManager(CustomerAdmin):
    pass


@admin.register(Project, site=admin_site)
class ProjectAdminForProjectManager(ProjectAdmin):
    pass


@admin.register(Task, site=admin_site)
class TaskAdminForProjectManager(TaskAdmin):
    pass


@admin.register(Epic, site=admin_site)
class EpicAdminForProjectManager(EpicAdmin):
    pass


@admin.register(OrderHistory, site=admin_site)
class OrderHistoryAdminForProjectManager(OrderHistoryAdmin):
    pass


@admin.register(Order, site=admin_site)
class OrderAdminForProjectManager(OrderAdmin):
    pass


@admin.register(Session, site=admin_site)
class SessionAdminForProjectManager(SessionAdmin):
    pass


@admin.register(Deposit, site=admin_site)
class DepositAdminForProjectManager(DepositAdmin):
    pass


@admin.register(Portfolio, site=admin_site)
class PortfolioAdminForProjectManager(PortfolioAdmin):
    pass


@admin.register(models.SessionSummaryByDays, site=admin_site)
class SessionSummaryByDaysAdmin(SummaryDailyAdmin):
    model = models.SessionSummaryByDays
    date_hierarchy = 'date'
    date_arg_name = 'date'
    title = 'Session summary'
    value_name = 'minutes_working'
    unit_name = 'hours'
    value_func = lambda self, x: round(x / 60, 1)  # NOQA
