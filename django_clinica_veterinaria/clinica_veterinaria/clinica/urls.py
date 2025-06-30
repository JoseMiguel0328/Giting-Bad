from django.urls import path
from . import views

urlpatterns = [
    path('landing', views.landing_page, name="landing"),
    path('services', views.services, name="services"),
    #Mascotas
    path('mascotas', views.gestionar_mascotas, name="gestionar_mascotas"),
    path('mascotas/crear/', views.crear_mascota, name="crear_mascota"),
    path('mascotas/editar/<int:pk>/', views.editar_mascota, name="editar_mascota"),
    path('mascotas/eliminar/<int:pk>/', views.eliminar_mascota, name="eliminar_mascota"),
    path('exportar/mascotas/', views.exportar_mascotas_csv, name='exportar_mascotas'),
    #Dueños
    path('duenos/', views.gestionar_duenos, name='gestionar_duenos'),
    path('duenos/crear/', views.crear_dueno, name='crear_dueno'),
    path('duenos/editar/<int:pk>/', views.editar_dueno, name='editar_dueno'),
    path('duenos/eliminar/<int:pk>/', views.eliminar_dueno, name='eliminar_dueno'),
    path('exportar/duenos/', views.exportar_duenos_csv, name='exportar_duenos'),
    #Veterinarios
    path('veterinarios/', views.gestionar_veterinarios, name='gestionar_veterinarios'),
    path('veterinarios/crear/', views.crear_veterinario, name='crear_veterinario'),
    path('veterinarios/editar/<int:pk>/', views.editar_veterinario, name='editar_veterinario'),
    path('veterinarios/eliminar/<int:pk>/', views.eliminar_veterinario, name='eliminar_veterinario'),
    path('exportar/veterinarios/', views.exportar_veterinarios_csv, name='exportar_veterinarios'),
    #Citas
    path('citas/', views.gestionar_citas, name='gestionar_citas'),
    path('citas/crear/', views.crear_cita, name='crear_cita'),
    path('citas/editar/<int:pk>/', views.editar_cita, name='editar_cita'),
    path('citas/eliminar/<int:pk>/', views.eliminar_cita, name='eliminar_cita'),
    path('exportar/citas/', views.exportar_citas_csv, name='exportar_citas'),
    #Medicamentos
    path('medicamentos/', views.gestionar_medicamentos, name='gestionar_medicamentos'),
    path('medicamentos/crear/', views.crear_medicamento, name='crear_medicamento'),
    path('medicamentos/editar/<int:pk>/', views.editar_medicamento, name='editar_medicamento'),
    path('medicamentos/eliminar/<int:pk>/', views.eliminar_medicamento, name='eliminar_medicamento'),
    path('exportar/medicamentos/', views.exportar_medicamentos_csv, name='exportar_medicamentos'),
    #Cirugia
    path('cirugias/', views.gestionar_cirugias, name='gestionar_cirugias'),
    path('cirugias/crear/', views.crear_cirugia, name='crear_cirugia'),
    path('cirugias/editar/<int:pk>/', views.editar_cirugia, name='editar_cirugia'),
    path('cirugias/eliminar/<int:pk>/', views.eliminar_cirugia, name='eliminar_cirugia'),
    path('exportar/cirugias/', views.exportar_cirugias_csv, name='exportar_cirugias'),
    #Exportar
    path('exportar/todo/', views.exportar_todo_csv_zip, name='exportar_todo'),
    #Bitacora
    path('bitacora/consulta/<int:consulta_id>/', views.crear_bitacora_consulta, name='crear_bitacora_consulta'),
    path('bitacora/detalle/<int:bitacora_id>/', views.detalle_bitacora_consulta, name='detalle_bitacora_consulta'),
    #Historial
    path('mascotas/historial/<int:mascota_id>/', views.exportar_historial_medico_pdf, name='exportar_historial_medico_pdf'),
]