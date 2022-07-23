# Generated by Django 4.0.5 on 2022-06-21 03:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('departamento', '0002_departamentomodel_delete_departamento'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonaModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=150, verbose_name='Nombres')),
                ('last_name', models.CharField(max_length=150, verbose_name='Apellidos')),
                ('job', models.CharField(choices=[('-1', 'Seleccionar'), ('0', 'Contador'), ('1', 'Administrador'), ('2', 'Sistemas'), ('3', 'Economista'), ('4', 'Otro')], default='-1', max_length=5, verbose_name='Cargo')),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='departamento.departamentomodel')),
            ],
        ),
    ]