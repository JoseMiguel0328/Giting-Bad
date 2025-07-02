# Gestor de Clínica Veterinaria

Este es un sistema de gestión para una clínica veterinaria desarrollado con Django, que permite registrar, consultar y administrar mascotas, dueños, y consultas clínicas. Se migró desde una versión basada en consola con almacenamiento en SQLite usando SQLAlchemy a una aplicación web con Django ORM y modelo MTV.

--------------------------
Características principales
--------------------------
- Registro y gestión de mascotas, dueños, veterinarios, medicamentos, cirugías y citas.
- Bitácora de consulta médica para cada cita.
- Exportación de historiales médicos en PDF.
- Exportación de datos en CSV y ZIP.
- Buscador dinámico en todas las tablas.
- Registro de logs de acciones importantes.
- Interfaz moderna y responsiva.

--------------------------
Requisitos previos
--------------------------
- Python 3.10 o superior
- pip (gestor de paquetes de Python)
- Virtualenv (opcional pero recomendado)

--------------------------
Instalación y ejecución
--------------------------
1. Clona o descarga este repositorio.
2. Abre una terminal y navega a la carpeta del proyecto.
3. (Opcional) Crea y activa un entorno virtual:
   - `python -m venv venv`
   - En Windows: `venv\Scripts\activate`
   - En Linux/Mac: `source venv/bin/activate`
4. Instala las dependencias:
   - `pip install -r requirements.txt`
5. Realiza las migraciones de la base de datos:
   - `python manage.py migrate`
6. (Opcional) Crea un superusuario para acceder al admin:
   - `python manage.py createsuperuser`
7. Ejecuta el servidor de desarrollo:
   - `python manage.py runserver`
8. Accede a la aplicación en tu navegador:
   - http://127.0.0.1:8000/app/landing

--------------------------
Notas adicionales
--------------------------
- Los archivos de logs se guardan en la carpeta `logs/`.
- Los archivos estáticos (CSS, imágenes) están en `clinica/static/`.
- Puedes personalizar la configuración en `clinica_veterinaria/settings.py`.
- Para soporte de PDF, asegúrate de tener instalado reportlab.

Proyecto académico - Gestión Clínica Veterinaria
