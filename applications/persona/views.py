from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

# import models
from .models import PersonaModel

# import forms
from applications.persona.forms import PersonaForm

TEMPLATE_ROUTE = 'persona'


class IndexView(TemplateView):
    """Home page"""
    template_name = 'index.html'


# 1. Listar todos los empleados de la empresa
class GetAll(ListView):
    """class that list all register"""
    template_name = f'{TEMPLATE_ROUTE}/list_all.html'

    # pagination
    paginate_by = 3
    ordering = ['id']

    # model = PersonaModel
    context_object_name = 'data'


    def get_queryset(self):
        # capturar los parametros 'params_query'
        str_kword = self.request.GET.get("kword", '')
        print(str_kword)
        lista = PersonaModel.objects.filter(
            full_name__icontains=str_kword
            # first_name=str_kword
        )
        return lista


# 2. Listar todos los empleados que pertenecen a un area de la empresa
class GetAllArea(ListView):
    template_name = f'{TEMPLATE_ROUTE}/list_area.html'
    context_object_name = 'data'

    # queryset: Puedo indicar con que caracteritica en especial me busque la info

    # recoger una parametro desde la URL
    def get_queryset(self):
        try:
            shortname_area = str(self.kwargs['shortname']).upper().strip()
            lista = PersonaModel.objects.filter(departamento__short_name=shortname_area if shortname_area else '')
        except Exception as e:
            print(e)
            lista = PersonaModel.objects.filter()
        return lista


# 3. listar empleados por palabra clave
class GetAllKword(ListView):
    template_name = f'{TEMPLATE_ROUTE}/list_kword.html'
    context_object_name = 'data'

    def get_queryset(self):
        # capturar los parametros 'params_query'
        str_kword = self.request.GET.get("kword", '')
        lista = PersonaModel.objects.filter(first_name=str_kword)
        print(lista)
        return lista


# 4. listar habilidades de un empleado
class GetAllSkill(ListView):
    template_name = f'{TEMPLATE_ROUTE}/list_skill.html'
    context_object_name = 'data'

    def get_queryset(self):
        persona = PersonaModel.objects.get(id=1)
        return persona.habilidad.all()


# 5. listar detalle de empleado
class DetailPersona(DetailView):
    template_name = f'{TEMPLATE_ROUTE}/detail.html'
    model = PersonaModel
    context_object_name = 'data'

    def get_context_data(self, **kwargs):
        context = super(DetailPersona, self).get_context_data(**kwargs)
        return context


class SuccessView(TemplateView):
    template_name = f"{TEMPLATE_ROUTE}/success.html"


# 6. create new a collaborate
class CreatePersonaView(CreateView):
    template_name = f'{TEMPLATE_ROUTE}/create.html'
    model = PersonaModel
    form_class = PersonaForm

    # template_name_suffix = '__create'

    # por campo
    # fields = ['first_name', 'last_name', 'job', 'departamento', 'habilidad', 'cv']

    # todos los objectos
    # fields = '__all__'
    # fields = ['first_name', 'last_name', 'job', 'departamento', 'habilidad', 'avatar']

    # success url: es el campo que redirecciona si paso satisfactoriamente
    # success_url = './success'
    success_url = reverse_lazy('persona_app:all-employed')  # permite buscar una url por la atiqueta name

    def form_valid(self, form):
        empleado = form.save(commit=False)
        empleado.full_name = f"{empleado.first_name} {empleado.last_name}"
        empleado.save()
        print(empleado)
        return super(CreatePersonaView, self).form_valid(form)


class PersonaUpdateView(UpdateView):
    """class that manage update a person"""
    template_name = f"{TEMPLATE_ROUTE}/update.html"
    model = PersonaModel
    success_url = reverse_lazy('persona_app:all-employed')

    # fields = '__all__'
    fields = ['first_name', 'last_name', 'job', 'departamento', 'habilidad']

    def post(self, request, *args, **kwargs):
        """ function that validate information before save in database"""
        # object = self.get_object()
        object_dict = request.POST
        print(f'****** >> Request: {object_dict}')
        for key in object_dict:
            print(f"{key}: {object_dict[key]}")
        return super().post(request, *args, **kwargs)


class PersonaDeleteView(DeleteView):
    """function that delete a register"""
    template_name = f"{TEMPLATE_ROUTE}/delete.html"
    model = PersonaModel
    success_url = reverse_lazy('persona_app:all-employed')
    context_object_name = 'item'
