from django.urls import path

from . import views

URL_BASE = "persona"
app_name = "persona_app"  # nombre del conjunto de la URL

urlpatterns = [
    path("", views.IndexView.as_view(), name='index'),
    path(f"{URL_BASE}/list",views.GetAll.as_view(),name='all-employed'),
    path(f"{URL_BASE}/by-area/", views.GetAllArea.as_view(), name='by-area'),
    path(f"{URL_BASE}/by-area/<shortname>", views.GetAllArea.as_view(), name='by-area-short'),
    path(f"{URL_BASE}/by-kword", views.GetAllKword.as_view()),
    path(f"{URL_BASE}/by-skills/", views.GetAllSkill.as_view()),
    path(f"{URL_BASE}/detail/<pk>", views.DetailPersona.as_view(), name='detail'),
    path(f"{URL_BASE}/create", views.CreatePersonaView.as_view(), name="create"),
    path(f"{URL_BASE}/success", views.SuccessView.as_view(), name='success'),
    path(f"{URL_BASE}/update/<pk>", views.PersonaUpdateView.as_view(), name='update'),
    path(f"{URL_BASE}/delete/<pk>", views.PersonaDeleteView.as_view(), name='delete'),
]
