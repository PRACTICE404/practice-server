from django.contrib import admin

from apps.customers.admin import CustomerAdmin
from apps.customers.models import Customer

from apps.projects.admin import ProjectAdmin
from apps.projects.models import Project

from apps.services.admin import (
    ServiceAdmin,
    PortfolioAdmin,
    FaqAdmin
)
from apps.services.models import (
    Service,
    Portfolio,
    Faq
)

from apps.marketplaces.admin import (
    MarketplaceAdmin,
    MarketplaceAccountAdmin,
    ProposalAdmin
)
from apps.marketplaces.models import (
    Marketplace,
    MarketplaceAccount,
    Proposal
)


class BusinessAnalystAdminSite(admin.AdminSite):
    site_header = 'Salesman'


admin_site = BusinessAnalystAdminSite(name='salesman')


@admin.register(Customer, site=admin_site)
class CustomerAdminForSalesman(CustomerAdmin):
    pass


@admin.register(Project, site=admin_site)
class ProjectAdminForSalesman(ProjectAdmin):
    pass


@admin.register(Service, site=admin_site)
class ServiceAdminForSalesman(ServiceAdmin):
    autocomplete_fields = ()
    readonly_fields = ('technology_areas',)

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False


@admin.register(Portfolio, site=admin_site)
class PortfolioAdminForSalesman(PortfolioAdmin):
    pass


@admin.register(Faq, site=admin_site)
class FaqAdminForSalesman(FaqAdmin):
    pass


@admin.register(Marketplace, site=admin_site)
class MarketplaceAdminForSalesman(MarketplaceAdmin):
    pass


@admin.register(MarketplaceAccount, site=admin_site)
class MarketplaceAccountAdminForSalesman(MarketplaceAccountAdmin):
    pass


@admin.register(Proposal, site=admin_site)
class ProposalAdminForSalesman(ProposalAdmin):
    pass
