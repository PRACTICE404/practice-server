import urllib.parse
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.shortcuts import redirect

from . import forms


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


class ContactsView(FormView):
    template_name = 'website/contacts/index.html'
    form_class = forms.WhatsAppForm

    def form_valid(self, form):
        full_name = form.cleaned_data["full_name"]
        phone = form.cleaned_data["phone"]
        company_type = form.cleaned_data["company_type"]
        budget = form.cleaned_data["budget"]
        message = form.cleaned_data["message"]

        # Начало сообщения
        initial_text = "Hello, I reached you from `aleksdev.xyz` website."

        # Полное сообщение
        text = f"{initial_text}\n\nFull Name: {full_name}\nPhone: `{phone}`\nCompany type: {company_type}\nBudget: {budget}$\n\n{message}"  # noqa
        encoded_text = urllib.parse.quote(text)

        whatsapp_url = f"https://api.whatsapp.com/send?phone=905349135639&text={encoded_text}"  # noqa
        return redirect(whatsapp_url)


class FaqView(TemplateView):
    template_name = 'website/maintenance.html'
