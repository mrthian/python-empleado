from django import forms
from applications.persona.models import PersonaModel


class PersonaForm(forms.ModelForm):

    class Meta:
        model = PersonaModel
        fields = (
            'first_name',
            'last_name',
            'job',
            'departamento',
            'avatar',
            'habilidad',
        )
        widgets = {
            'habilidad': forms.CheckboxSelectMultiple()
        }
