from django.urls import path

from .marketer.admin import admin_site as marketer_admin_site
from .project_manager.admin import admin_site as project_manager_admin_site


urlpatterns = (
    path('admin/marketer/', marketer_admin_site.urls),
    path('admin/project_manager/', project_manager_admin_site.urls)
)
