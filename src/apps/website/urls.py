from django.urls import path

from . import views

urlpatterns = (
    path('', views.HomeView.as_view(), name='home'),
    path('services/', views.ServicesView.as_view(), name='service-list'),
    path(
        'technologies/',
        views.TechnologiesListView.as_view(),
        name='technology-list'
    ),
    path('portfolio/', views.PortfolioView.as_view(), name='portfolio-list'),
    path('portfolio-detail/', views.PortfolioDetailView.as_view(), name='portfolio-detail'),  # noqa
    path('blog/', views.BlogView.as_view(), name='post-list'),
    path('blog-detail/', views.BlogDetailView.as_view(), name='post-detail'),
    path('plans/', views.PlansView.as_view(), name='plan-list'),
    path('contacts/', views.ContactsView.as_view(), name='contacts')
)
