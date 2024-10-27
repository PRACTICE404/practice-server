from django.contrib import admin

from apps.customers.admin import CustomerAdmin
from apps.customers.models import Customer

from apps.marketplaces.admin import MarketplaceAdmin, MarketplaceAccountAdmin
from apps.marketplaces.models import Marketplace, MarketplaceAccount

from apps.services.admin import (
    ProgrammingLanguageAdmin,
    TechnologyAdmin,
    TechnologyAreaAdmin,
    ServiceAdmin,
    FaqAdmin,
    PortfolioAdmin
)
from apps.services.models import (
    ProgrammingLanguage,
    Technology,
    TechnologyArea,
    Service,
    Faq,
    Portfolio
)

from apps.posts.admin import (
    PostBranchAdmin,
    PostCategoryAdmin,
    PostTagAdmin,
    PostAdmin,
    PostIdeaAdmin
)
from apps.posts.models import (
    PostBranch,
    PostCategory,
    PostTag,
    Post,
    PostIdea
)


class MarketerAdminSite(admin.AdminSite):
    site_header = 'Marketer'


admin_site = MarketerAdminSite(name='marketer')


@admin.register(Customer, site=admin_site)
class CustomerAdminForMarketer(CustomerAdmin):
    pass


@admin.register(Marketplace, site=admin_site)
class MarketplaceAdminForCustomer(MarketplaceAdmin):
    pass


@admin.register(MarketplaceAccount, site=admin_site)
class MarketplaceAccountAdminForCustomer(MarketplaceAccountAdmin):
    pass


@admin.register(ProgrammingLanguage, site=admin_site)
class ProgrammingLanguageAdminForMarketer(ProgrammingLanguageAdmin):
    pass


@admin.register(Technology, site=admin_site)
class TechnologyAdminForMarketer(TechnologyAdmin):
    pass


@admin.register(TechnologyArea, site=admin_site)
class TechnologyAreaAdminForMarketer(TechnologyAreaAdmin):
    pass


@admin.register(Service, site=admin_site)
class ServiceAdminForMarketer(ServiceAdmin):
    pass


@admin.register(Faq, site=admin_site)
class FaqAdminForMarketer(FaqAdmin):
    pass


@admin.register(Portfolio, site=admin_site)
class PortfolioAdminForMarketer(PortfolioAdmin):
    autocomplete_fields = ()
    exclude = ('project',)


@admin.register(PostBranch, site=admin_site)
class PostBranchAdminForMarketer(PostBranchAdmin):
    pass


@admin.register(PostCategory, site=admin_site)
class PostCategoryAdminForMarketer(PostCategoryAdmin):
    pass


@admin.register(PostTag, site=admin_site)
class PostTagAdminForMarketer(PostTagAdmin):
    pass


@admin.register(Post, site=admin_site)
class PostAdminForMarketer(PostAdmin):
    pass


@admin.register(PostIdea, site=admin_site)
class PostIdeaAdminForMarketer(PostIdeaAdmin):
    pass
