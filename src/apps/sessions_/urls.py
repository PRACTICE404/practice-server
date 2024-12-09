from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register(r"(?P<id>\d*)/signals", views.SignalBySessionViewSet, basename='signals-by-session')  # noqa
router.register(r"signals", views.SignalViewSet)  # noqa
router.register(r"", views.SessionViewSet)


urlpatterns = (
    path("", include(router.urls)),
)
