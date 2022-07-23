from django.contrib import admin
from django.urls import path, re_path

from .views import *

URL_BASE = "departamento"
app_name = 'departamento_app'


urlpatterns = [
    # path("departamento/", admin.site.urls, name=''),
    path(f"{URL_BASE}/", DepartamentoIndexView.as_view(), name='index'),
    path(f"{URL_BASE}/create", DepartamentoCreateView.as_view(), name='create'),
]
