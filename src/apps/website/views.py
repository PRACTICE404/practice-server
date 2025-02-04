from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'website/home/index.html'


class ServicesView(TemplateView):
    template_name = 'website/services/index.html'


class TechnologiesListView(TemplateView):
    template_name = 'website/technologies/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['objects_technology'] = Technology.objects.all()  # noqa
        return context


class PortfolioView(TemplateView):
    template_name = 'website/portfolio/index.html'


class PortfolioDetailView(TemplateView):
    template_name = 'website/portfolio-detail/index.html'


class BlogView(TemplateView):
    template_name = 'website/blog/index.html'


class BlogDetailView(TemplateView):
    template_name = 'website/blog-detail/index.html'


class PlansView(TemplateView):
    template_name = 'website/plans/index.html'


class ContactsView(TemplateView):
    template_name = 'website/contacts/index.html'
