from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import HomeModel
from .forms import HomeForm

TEMPLATE_ROUTE = 'home'


class HomeIndexView(ListView):
    """class that manage index"""
    template_name = f"{TEMPLATE_ROUTE}/index.html"
    model = HomeModel
    context_object_name = 'data'
    ordering = ['id']


class HomeDetailView(DetailView):
    """class that mananage detail of a HomeModel"""
    template_name = f"{TEMPLATE_ROUTE}/detail.html"
    model = HomeModel


class HomeSuccessView(TemplateView):
    template_name = f"{TEMPLATE_ROUTE}/success.html"


class HomeCreateView(CreateView):
    template_name = f"{TEMPLATE_ROUTE}/create.html"
    model = HomeModel
    # fields = '__all__'
    form_class = HomeForm
    success_url = reverse_lazy('home_app:index')


class HomeUpdateView(UpdateView):
    template_name = f"{TEMPLATE_ROUTE}/update.html"
    model = HomeModel
    fields = '__all__'
    success_url = reverse_lazy('home_app:index')


class HomeDeleteView(DeleteView):
    template_name = f"{TEMPLATE_ROUTE}/delete.html"
    model = HomeModel
    success_url = reverse_lazy('home_app:index')
    context_object_name = 'item'


class HomeFoundationView(TemplateView):
    template_name = f"{TEMPLATE_ROUTE}/resumen-foundation.html"


class HomeHome1View(TemplateView):
    template_name = f"{TEMPLATE_ROUTE}/home1.html"


class HomeHome2View(TemplateView):
    template_name = f"{TEMPLATE_ROUTE}/home2.html"


class HomeHome3View(TemplateView):
    template_name = f"{TEMPLATE_ROUTE}/home3.html"
