# Gestor de Clínica Veterinaria

Este es un sistema de gestión para una clínica veterinaria desarrollado con Django, que permite registrar, consultar y administrar mascotas, dueños, y consultas clínicas. Se migró desde una versión basada en consola con archivos CSV a una aplicación web con almacenamiento en SQLite usando SQLAlchemy para pruebas y Django ORM para la aplicación final.

## Características principales

- Registro y listado de mascotas
- Registro y administración de dueños
- Creación y listado de consultas veterinarias
- Validaciones de entrada (edad, nombre, etc.)
- Tests automatizados con `unittest`
- Interfaz web con Django

## Estructura del proyecto

```
django_clinica_veterinaria/
├── manage.py
├── requirements.txt
├── README.md
├── apps/
│   ├── gestion/
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── forms.py
│   │   ├── urls.py
│   │   └── templates/...
├── models/
│   ├── mascota.py
│   ├── dueno.py
│   └── consulta.py
├── services/
│   ├── gestion.py
│   └── persistencia.py
├── tests/
│   ├── test_gestion.py
│   ├── test_mascota.py
│   └── ...
```

## Instalación y ejecución

1. Clona el repositorio:
```bash
git clone https://github.com/usuario/django_clinica_veterinaria.git
cd django_clinica_veterinaria
```

2. Instala dependencias:
```bash
pip install -r requirements.txt
```

3. Ejecuta migraciones:
```bash
python manage.py migrate
```

4. Corre el servidor de desarrollo:
```bash
python manage.py runserver
```

## Dependencias principales
- Django >= 4.0
- SQLAlchemy >= 2.0
- unittest (incluido en la librería estándar de Python)

## Notas adicionales
- Puedes crear superusuarios para administrar desde el panel de Django Admin.
- Los datos originalmente se guardaban en CSV, pero ahora se gestionan vía base de datos con modelos ORM.
- Se recomienda organizar los formularios en una carpeta `forms/` si hay múltiples formularios complejos.

---

Proyecto académico - Gestión Clínica Veterinaria
