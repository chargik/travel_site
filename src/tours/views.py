from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView

from lead.forms import JoinForm
from .models import Tours

# Create your views here.
class HomeView(ListView):
    queryset = Tours.objects.all()
    template_name = 'home.html'
    form_class = JoinForm

    def get_queryset(self):
        slug = self.kwargs.get("slug")
        queryset = Tours.objects.all()
        return queryset

    def get_success_message(self, cleaned_data):
        print(cleaned_data)
        return "Спасибо, наш менеджер свяжется с Вами!"


class TourDetailView(DetailView, SuccessMessageMixin, CreateView):
    template_name = 'tours/tours_detail.html'
    queryset = Tours.objects.all()
    form_class = JoinForm
    # success_url = objects.get_absolute_url()
    # success_url = "/{slug}/"


    # def get_context_data(self, *args, **kwargs):
    #     context = super(TourDetailView, self).get_context_data(*args, **kwargs)
    #     context['obj'] = Tours.objects.all().first()
    #     return context

    def get_success_message(self, cleaned_data):
        print(cleaned_data)
        return "Спасибо, наш менеджер свяжется с Вами!"