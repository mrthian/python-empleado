# paquete que ayuda a crear formularios
from django import forms

from .models import HomeModel


class HomeForm(forms.ModelForm):

    class Meta:
        model = HomeModel
        # fields: es para indicar que campos queremos mostrar
        fields = ('titulo', 'subtitulo', 'cantidad')

        # para personalizar campos
        widgets = {
            'titulo': forms.TextInput(
                attrs={
                    'placeholder': "Ingresar titulo",
                    'class': "form-control"
                }
            ),
            'subtitulo': forms.TextInput(
                attrs={
                    'placeholder': 'Ingresar titulo corto',
                    'class': 'form-control'
                }
            ),
        }

        labels = {
            'titulo': 'Ingresar Titulo',
            'subtitulo': 'Ingresar Subtitulo',
            'cantidad': 'Ingreasr una cantidad'
        }


    # add validation
    def clean_cantidad(self):
        # get values of a field, example: cantidad
        cant = self.cleaned_data['cantidad']
        print(cant)
        if cant < 10:
            raise forms.ValidationError(message='quantity invalid')
        return cant
