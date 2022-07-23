from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import FormView

from applications.persona.models import PersonaModel
from .models import DepartamentoModel
from .forms import DepartamentoForm

TEMPLATE_ROUTE = 'departamento'


class DepartamentoIndexView(ListView):
    template_name = f"{TEMPLATE_ROUTE}/index.html"
    model = DepartamentoModel
    context_object_name = 'data'
    ordering = ['id']


# Create your views here.
class DepartamentoCreateView(FormView):
    template_name = f"{TEMPLATE_ROUTE}/create.html"
    form_class = DepartamentoForm
    success_url = reverse_lazy('departamento_app:index')

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        dpto = DepartamentoModel(
            name=form.cleaned_data['departamento'],
            short_name=form.cleaned_data['shortname'],
            state=True
        )
        print(f"=====>> {dpto}")
        if dpto.id is None:
            dpto.save()

        print(f'Id Dpto: {dpto.id}')

        PersonaModel.objects.create(
            first_name=form.cleaned_data['nombres'],
            last_name=form.cleaned_data['apellidos'],
            job='1',
            departamento=dpto
        )

        print('end ---> save')

        return super().form_valid(form)
