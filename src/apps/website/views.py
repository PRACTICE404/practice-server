from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'website/home/index.html'


class ServicesView(TemplateView):
    template_name = 'website/maintenance.html'


class TechnologiesListView(TemplateView):
    template_name = 'website/maintenance.html'


class PortfolioView(TemplateView):
    template_name = 'website/maintenance.html'


class PortfolioDetailView(TemplateView):
    template_name = 'website/maintenance.html'


class BlogView(TemplateView):
    template_name = 'website/maintenance.html'


class BlogDetailView(TemplateView):
    template_name = 'website/maintenance.html'


class PlansView(TemplateView):
    template_name = 'website/maintenance.html'


class ContactsView(TemplateView):
    template_name = 'website/contacts/index.html'
