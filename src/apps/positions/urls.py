from django.urls import path

from .marketer.admin import admin_site as marketer_admin_site


urlpatterns = (
    path('admin/marketer/', marketer_admin_site.urls),
)
