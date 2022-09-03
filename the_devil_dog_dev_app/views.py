from django.views.generic import TemplateView, DetailView

from .models import Service

class HomePageView(TemplateView):
    template_name = 'home.html'

class ServiceDetailView(DetailView):
    model = Service
    template_name = 'templates/service_detail.html'