import uuid
from django.contrib import admin
from .models import PersonaModel, HabilidadModel

# Register your models here.
admin.site.register(HabilidadModel)


class PersonaAdmin(admin.ModelAdmin):
    "Listar lo que quiero que muestre el administador"
    list_display = (
        'first_name',
        'last_name',
        'job',
        'departamento',
        'full_name',
        'code',
        'id',
        'full_name'
    )

    # campos calculados
    def full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"

    def code(self, obj):
        return uuid.uuid4()


    search_fields = ('first_name', )
    list_filter = ('departamento', 'job', 'habilidad')
    # personalizar filter de habilidades, dado que puede ser extendo en relaciones many-to-many
    filter_horizontal = ('habilidad', )


# con esto le decimos que queremos ver como una tabla
admin.site.register(PersonaModel, PersonaAdmin)
