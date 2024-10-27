from django.urls import path

from .developer.admin import admin_site as developer_admin_site
from .finance_manager.admin import admin_site as finance_manager_admin_site
from .marketer.admin import admin_site as marketer_admin_site
from .project_manager.admin import admin_site as project_manager_admin_site
from .salesman.admin import admin_site as salesman_admin_site


urlpatterns = (
    path('admin/developer/', developer_admin_site.urls),
    path('admin/finance_manager/', finance_manager_admin_site.urls),
    path('admin/marketer/', marketer_admin_site.urls),
    path('admin/project_manager/', project_manager_admin_site.urls),
    path('admin/salesman/', salesman_admin_site.urls)
)
