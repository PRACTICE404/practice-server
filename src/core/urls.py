from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('apps.website.urls')),
    path('', include('apps.positions.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('api/customers/', include('apps.customers.urls')),
    path('api/sessions/', include('apps.sessions_.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # NOQA
