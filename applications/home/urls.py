from django.contrib import admin
from django.urls import path

from . import views

URL_BASE = "home"
app_name = "home_app"

urlpatterns = [
    path(f"{URL_BASE}/", views.HomeIndexView.as_view(), name='index'),
    path(f"{URL_BASE}/detail/<pk>", views.HomeDetailView.as_view(), name='detail'),
    path(f"{URL_BASE}/success", views.HomeSuccessView.as_view(), name='success'),
    path(f"{URL_BASE}/create", views.HomeCreateView.as_view(), name='create'),
    path(f"{URL_BASE}/update/<pk>", views.HomeUpdateView.as_view(), name='update'),
    path(f"{URL_BASE}/delete/<pk>", views.HomeDeleteView.as_view(), name='delete'),
    path(f"{URL_BASE}/resume-foundation", views.HomeFoundationView.as_view(), name='resume-foundation'),
    path(f"{URL_BASE}/home1", views.HomeHome1View.as_view(), name='home1'),
    path(f"{URL_BASE}/home2", views.HomeHome2View.as_view(), name='home2'),
    path(f"{URL_BASE}/home3", views.HomeHome3View.as_view(), name='home3'),
]
