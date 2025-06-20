from django.urls import path
from . import views

urlpatterns = [
    path('landing', views.landing_page, name="landing"),
    path('services', views.services, name="services"),
    path('mascotas', views.gestionar_mascotas, name="gestionar_mascotas"),
    path('mascotas/crear/', views.crear_mascota, name="crear_mascota"),
    path('mascotas/editar/<int:pk>/', views.editar_mascota, name="editar_mascota"),
    path('mascotas/eliminar/<int:pk>/', views.eliminar_mascota, name="eliminar_mascota"),
    path('duenos/', views.gestionar_duenos, name='gestionar_duenos'),
    path('duenos/crear/', views.crear_dueno, name='crear_dueno'),
    path('duenos/editar/<int:pk>/', views.editar_dueno, name='editar_dueno'),
    path('duenos/eliminar/<int:pk>/', views.eliminar_dueno, name='eliminar_dueno'),
    path('citas/', views.gestionar_citas, name='gestionar_citas'),
    path('citas/crear/', views.crear_cita, name='crear_cita'),
    path('citas/editar/<int:pk>/', views.editar_cita, name='editar_cita'),
    path('citas/eliminar/<int:pk>/', views.eliminar_cita, name='eliminar_cita'),
]