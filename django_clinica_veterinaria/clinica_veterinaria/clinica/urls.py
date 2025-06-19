from django.urls import path
from . import views

urlpatterns = [
    path('landing', views.landing_page, name="landing"),
    path('services', views.services, name="services"),
    path('mascotas/crear/', views.crear_mascota, name='crear_mascota'),
    path('mascotas/', views.listar_mascotas, name='listar_mascotas'),
]