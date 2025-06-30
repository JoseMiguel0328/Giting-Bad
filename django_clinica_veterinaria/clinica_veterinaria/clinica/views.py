# Standard library imports
import csv
import io
import zipfile
import os

# Django imports
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.utils import timezone
from django.conf import settings

# App imports
from .models.mascota import Mascota
from .forms.mascota_form import MascotaForm
from .models.dueno import Dueno
from .forms.dueno_form import DuenoForm
from .models.consulta import Consulta
from .forms.consulta_form import ConsultaForm
from .models.medicamento import Medicamento
from .forms.medicamento_form import MedicamentoForm
from .models.veterinario import Veterinario
from .forms.veterinario_form import VeterinarioForm
from .models.cirugia import Cirugia
from .forms.cirugia_form import CirugiaForm
from .models.bitacora_consulta import BitacoraConsulta
from .forms.bitacora_form import BitacoraConsultaForm

#Util imports
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import ImageReader



def hello_world(request):
    return HttpResponse("Hello World")

class hello_colombia(View):
    def get(self, request):
        return HttpResponse("Hello Colombia")
    
def landing_page(request):
    return render(request, 'clinica/index.html')

def services(request):
    return render(request, 'clinica/services.html')

#------------------------------------------------------Mascotas------------------------------------------------------
def gestionar_mascotas(request):
    mascotas = Mascota.objects.all().select_related('dueno')

    if request.method == 'POST':
        form = MascotaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gestionar_mascotas')
    else:
        form = MascotaForm()

    context = {
        'mascotas': mascotas,
        'form': form
    }
    return render(request, 'clinica/mascotas.html', context)

def crear_mascota(request):
    if request.method == 'POST':
        form = MascotaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gestionar_mascotas')
    else:
        form = MascotaForm()
    return render(request, 'clinica/crear_mascota.html', {'form': form})

def editar_mascota(request, pk):
    mascota = get_object_or_404(Mascota, pk=pk)
    if request.method == 'POST':
        form = MascotaForm(request.POST, instance=mascota)
        if form.is_valid():
            form.save()
            return redirect('gestionar_mascotas')
    else:
        form = MascotaForm(instance=mascota)
    return render(request, 'clinica/editar_mascota.html', {'form': form})

def eliminar_mascota(request, pk):
    mascota = get_object_or_404(Mascota, pk=pk)
    if request.method == 'POST':
        mascota.delete()
        return redirect('gestionar_mascotas')
    return render(request, 'clinica/eliminar_mascota.html', {'mascota': mascota})

def exportar_mascotas_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="mascotas.csv"'

    writer = csv.writer(response)
    writer.writerow(['Nombre', 'Especie', 'Raza', 'Edad', 'Dueño'])

    for mascota in Mascota.objects.all():
        writer.writerow([
            mascota.nombre,
            mascota.especie,
            mascota.raza,
            mascota.edad,
            mascota.dueno.nombre if mascota.dueno else "Sin dueño"
        ])

    return response

#------------------------------------------------------Veterinarios------------------------------------------------------

def gestionar_veterinarios(request):
    veterinarios = Veterinario.objects.all()
    return render(request, 'clinica/veterinarios.html', {'veterinarios': veterinarios})

def crear_veterinario(request):
    if request.method == 'POST':
        form = VeterinarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gestionar_veterinarios')
    else:
        form = VeterinarioForm()
    return render(request, 'clinica/crear_veterinario.html', {'form': form})

def editar_veterinario(request, pk):
    veterinario = get_object_or_404(Veterinario, pk=pk)
    if request.method == 'POST':
        form = VeterinarioForm(request.POST, instance=veterinario)
        if form.is_valid():
            form.save()
            return redirect('gestionar_veterinarios')
    else:
        form = VeterinarioForm(instance=veterinario)
    return render(request, 'clinica/crear_veterinario.html', {'form': form})  # Reutiliza template

def eliminar_veterinario(request, pk):
    veterinario = get_object_or_404(Veterinario, pk=pk)
    if request.method == 'POST':
        veterinario.delete()
        return redirect('gestionar_veterinarios')
    return render(request, 'clinica/eliminar_veterinario.html', {'veterinario': veterinario})

def exportar_veterinarios_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="veterinarios.csv"'

    writer = csv.writer(response)
    writer.writerow(['Nombre', 'Documento', 'Teléfono', 'Especialidad'])

    for vet in Veterinario.objects.all():
        writer.writerow([vet.nombre, vet.documento, vet.telefono, vet.especialidad])

    return response

#------------------------------------------------------Dueños------------------------------------------------------

def gestionar_duenos(request):
    duenos = Dueno.objects.all()
    return render(request, 'clinica/duenos.html', {'duenos': duenos})

def crear_dueno(request):
    if request.method == 'POST':
        form = DuenoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gestionar_duenos')
    else:
        form = DuenoForm()
    return render(request, 'clinica/crear_dueno.html', {'form': form})

def editar_dueno(request, pk):
    dueno = get_object_or_404(Dueno, pk=pk)
    if request.method == 'POST':
        form = DuenoForm(request.POST, instance=dueno)
        if form.is_valid():
            form.save()
            return redirect('gestionar_duenos')
    else:
        form = DuenoForm(instance=dueno)
    return render(request, 'clinica/crear_dueno.html', {'form': form})

def eliminar_dueno(request, pk):
    dueno = get_object_or_404(Dueno, pk=pk)
    if request.method == 'POST':
        dueno.delete()
        return redirect('gestionar_duenos')
    return render(request, 'clinica/eliminar_dueno.html', {'dueno': dueno})

def exportar_duenos_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="duenos.csv"'

    writer = csv.writer(response)
    writer.writerow(['Nombre', 'Documento', 'Teléfono', 'Dirección'])

    for dueno in Dueno.objects.all():
        writer.writerow([dueno.nombre, dueno.documento, dueno.telefono, dueno.direccion])

    return response

#------------------------------------------------------Citas------------------------------------------------------

def gestionar_citas(request):
    citas = Consulta.objects.all()
    return render(request, 'clinica/citas.html', {'citas': citas})

def crear_cita(request):
    if request.method == 'POST':
        form = ConsultaForm(request.POST)
        if form.is_valid():
            form.save()
            consulta = form.save()
            return redirect('crear_bitacora_consulta', consulta_id=consulta.id)
    else:
        form = ConsultaForm()
    return render(request, 'clinica/crear_cita.html', {'form': form})

def editar_cita(request, pk):
    consulta = get_object_or_404(Consulta, pk=pk)
    if request.method == 'POST':
        form = ConsultaForm(request.POST, instance=consulta)
        if form.is_valid():
            form.save()
            return redirect('gestionar_citas')
    else:
        form = ConsultaForm(instance=consulta)
    return render(request, 'clinica/editar_cita.html', {'form': form})

def eliminar_cita(request, pk):
    consulta = get_object_or_404(Consulta, pk=pk)
    if request.method == 'POST':
        consulta.delete()
        return redirect('gestionar_citas')
    return render(request, 'clinica/eliminar_cita.html', {'consulta': consulta})

def exportar_citas_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="consultas.csv"'

    writer = csv.writer(response)
    writer.writerow(['Fecha', 'Motivo', 'Diagnóstico', 'Mascota'])

    for consulta in Consulta.objects.all():
        writer.writerow([
            consulta.fecha,
            consulta.motivo,
            consulta.diagnostico,
            consulta.mascota.nombre if consulta.mascota else "Sin mascota"
        ])

    return response

#------------------------------------------------------Medicamentos------------------------------------------------------

def gestionar_medicamentos(request):
    medicamentos = Medicamento.objects.all()

    if request.method == 'POST':
        form = MedicamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gestionar_medicamentos')
    else:
        form = MedicamentoForm()

    context = {
        'medicamentos': medicamentos,
        'form': form,
        'hoy': timezone.now().date()
    }
    return render(request, 'clinica/medicamentos.html', context)

def crear_medicamento(request):
    if request.method == 'POST':
        form = MedicamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gestionar_medicamentos')
    else:
        form = MedicamentoForm()
    return render(request, 'clinica/crear_medicamento.html', {'form': form})

def editar_medicamento(request, pk):
    medicamento = get_object_or_404(Medicamento, pk=pk)
    if request.method == 'POST':
        form = MedicamentoForm(request.POST, instance=medicamento)
        if form.is_valid():
            form.save()
            return redirect('gestionar_medicamentos')
    else:
        form = MedicamentoForm(instance=medicamento)
    return render(request, 'clinica/editar_medicamento.html', {'form': form})

def eliminar_medicamento(request, pk):
    medicamento = get_object_or_404(Medicamento, pk=pk)
    if request.method == 'POST':
        medicamento.delete()
        return redirect('gestionar_medicamentos')
    return render(request, 'clinica/eliminar_medicamento.html', {'medicamento': medicamento})

def exportar_medicamentos_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="medicamentos.csv"'

    writer = csv.writer(response)
    writer.writerow(['Nombre', 'Descripción', 'Cantidad Disponible', 'Fecha de Vencimiento'])

    for med in Medicamento.objects.all():
        writer.writerow([med.nombre, med.descripcion, med.cantidad_disponible, med.fecha_vencimiento])

    return response

#------------------------------------------------------Cirugia------------------------------------------------------

def gestionar_cirugias(request):
    cirugias = Cirugia.objects.select_related('mascota', 'veterinario').all()
    return render(request, 'clinica/cirugias.html', {'cirugias': cirugias})

def crear_cirugia(request):
    if request.method == 'POST':
        form = CirugiaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gestionar_cirugias')
    else:
        form = CirugiaForm()
    return render(request, 'clinica/crear_cirugia.html', {'form': form})

def editar_cirugia(request, pk):
    cirugia = get_object_or_404(Cirugia, pk=pk)
    if request.method == 'POST':
        form = CirugiaForm(request.POST, instance=cirugia)
        if form.is_valid():
            form.save()
            return redirect('gestionar_cirugias')
    else:
        form = CirugiaForm(instance=cirugia)
    return render(request, 'clinica/editar_cirugia.html', {'form': form})

def eliminar_cirugia(request, pk):
    cirugia = get_object_or_404(Cirugia, pk=pk)
    if request.method == 'POST':
        cirugia.delete()
        return redirect('gestionar_cirugias')
    return render(request, 'clinica/eliminar_cirugia.html', {'cirugia': cirugia})

def exportar_cirugias_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="cirugias.csv"'

    writer = csv.writer(response)
    writer.writerow(['Nombre', 'Descripción', 'Fecha', 'Mascota', 'Veterinario'])

    for cirugia in Cirugia.objects.all():
        writer.writerow([
            cirugia.nombre,
            cirugia.descripcion,
            cirugia.fecha,
            cirugia.mascota.nombre if cirugia.mascota else "Sin mascota",
            cirugia.veterinario.nombre if cirugia.veterinario else "Sin veterinario"
        ])

    return response

#------------------------------------------------------CSV------------------------------------------------------

def exportar_todo_csv_zip(request):
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, 'w') as zip_file:

        # Veterinarios
        veterinarios_io = io.StringIO()
        writer = csv.writer(veterinarios_io)
        writer.writerow(['ID', 'Nombre', 'Documento', 'Teléfono', 'Especialidad'])
        for v in Veterinario.objects.all():
            writer.writerow([v.id, v.nombre, v.documento, v.telefono, v.especialidad])
        zip_file.writestr('veterinarios.csv', veterinarios_io.getvalue())

        # Dueños
        duenos_io = io.StringIO()
        writer = csv.writer(duenos_io)
        writer.writerow(['ID', 'Nombre', 'Documento', 'Teléfono', 'Dirección'])
        for d in Dueno.objects.all():
            writer.writerow([d.id, d.nombre, d.documento, d.telefono, d.direccion])
        zip_file.writestr('duenos.csv', duenos_io.getvalue())

        # Mascotas
        mascotas_io = io.StringIO()
        writer = csv.writer(mascotas_io)
        writer.writerow(['ID', 'Nombre', 'Especie', 'Raza', 'Edad', 'Dueño'])
        for m in Mascota.objects.all():
            writer.writerow([m.id, m.nombre, m.especie, m.raza, m.edad, m.dueno.nombre])
        zip_file.writestr('mascotas.csv', mascotas_io.getvalue())

        # Consultas
        consultas_io = io.StringIO()
        writer = csv.writer(consultas_io)
        writer.writerow(['ID', 'Fecha', 'Motivo', 'Diagnóstico', 'Mascota'])
        for c in Consulta.objects.all():
            writer.writerow([c.id, c.fecha, c.motivo, c.diagnostico, c.mascota.nombre])
        zip_file.writestr('consultas.csv', consultas_io.getvalue())

        # Medicamentos
        medicamentos_io = io.StringIO()
        writer = csv.writer(medicamentos_io)
        writer.writerow(['ID', 'Nombre', 'Descripción', 'Cantidad', 'Vencimiento'])
        for m in Medicamento.objects.all():
            writer.writerow([m.id, m.nombre, m.descripcion, m.cantidad_disponible, m.fecha_vencimiento])
        zip_file.writestr('medicamentos.csv', medicamentos_io.getvalue())

        # Cirugías
        cirugias_io = io.StringIO()
        writer = csv.writer(cirugias_io)
        writer.writerow(['ID', 'Descripción', 'Fecha', 'Mascota', 'Veterinario'])
        for c in Cirugia.objects.all():
            vet_nombre = c.veterinario.nombre if c.veterinario else 'No asignado'
            writer.writerow([c.id, c.descripcion, c.fecha, c.mascota.nombre, vet_nombre])
        zip_file.writestr('cirugias.csv', cirugias_io.getvalue())

    buffer.seek(0)
    response = HttpResponse(buffer, content_type='application/zip')
    response['Content-Disposition'] = 'attachment; filename="datos_clinica.zip"'
    return response

#------------------------------------------------------Bitacora------------------------------------------------------

def crear_bitacora_consulta(request, consulta_id):
    consulta = get_object_or_404(Consulta, pk=consulta_id)
    mascota = consulta.mascota
    dueno = mascota.dueno

    if request.method == 'POST':
        form = BitacoraConsultaForm(request.POST)
        if form.is_valid():
            bitacora = form.save(commit=False)
            bitacora.consulta = consulta
            bitacora.mascota = mascota
            bitacora.dueno = dueno
            bitacora.save()
            form.save_m2m()
            return redirect('detalle_bitacora_consulta', bitacora.id)
    else:
        form = BitacoraConsultaForm(initial={
            'diagnostico': consulta.diagnostico,
            'tratamiento': '',  
            'observaciones': '',
        })

    context = {
        'form': form,
        'consulta': consulta,
        'mascota': mascota,
        'dueno': dueno,
    }
    return render(request, 'clinica/bitacora_consulta_form.html', context)

def detalle_bitacora_consulta(request, bitacora_id):
    bitacora = get_object_or_404(BitacoraConsulta, pk=bitacora_id)
    return render(request, 'clinica/bitacora_consulta_detalle.html', {'bitacora': bitacora})

#------------------------------------------------------Historial------------------------------------------------------

def exportar_historial_medico_pdf(request, mascota_id):
    mascota = get_object_or_404(Mascota, pk=mascota_id)
    bitacoras = mascota.bitacoraconsulta_set.select_related('consulta', 'veterinario').all().order_by('consulta__fecha')

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="historial_{mascota.nombre}.pdf"'

    # Registrar fuentes Montserrat
    font_dir = os.path.join(settings.BASE_DIR, 'clinica', 'static', 'fonts')
    pdfmetrics.registerFont(TTFont('Montserrat', os.path.join(font_dir, 'Montserrat-Regular.ttf')))
    pdfmetrics.registerFont(TTFont('Montserrat-Bold', os.path.join(font_dir, 'Montserrat-Bold.ttf')))

    # Colores personalizados
    verde_principal = colors.HexColor("#93C572")
    blanco = colors.white

    # Logo
    logo_path = os.path.join(settings.BASE_DIR, 'clinica', 'static', 'img', 'logo.png')
    logo = None
    if os.path.exists(logo_path):
        logo = ImageReader(logo_path)

    p = canvas.Canvas(response, pagesize=letter)
    width, height = letter

    def dibujar_marca_agua():
        if logo:
            p.saveState()
            p.translate(width/2 - 125, height/2 - 125)
            p.drawImage(logo, 0, 0, width=250, height=250, mask='auto')
            p.restoreState()

    def dibujar_encabezado():
        p.setFillColor(verde_principal)
        p.rect(0, height-60, width, 60, fill=1, stroke=0)
        p.setFillColor(blanco)
        p.setFont("Montserrat-Bold", 22)
        p.drawString(50, height-40, "Clínica Veterinaria Mi Mascota")

    def dibujar_pie():
        fecha = timezone.now().strftime("%d/%m/%Y %H:%M")
        p.setFont("Montserrat", 10)
        p.setFillColor(colors.grey)
        p.drawString(50, 30, f"Generado el {fecha}")

    # Página 1
    dibujar_marca_agua()
    dibujar_encabezado()

    y = height - 80
    p.setFont("Montserrat-Bold", 16)
    p.setFillColor(colors.black)
    p.drawString(50, y, f"Historial Médico de {mascota.nombre}")
    y -= 25

    p.setFont("Montserrat", 12)
    p.drawString(50, y, f"Especie: {mascota.especie}  |  Raza: {mascota.raza}  |  Edad: {mascota.edad}")
    y -= 18
    p.drawString(50, y, f"Dueño: {mascota.dueno.nombre}  |  Tel: {mascota.dueno.telefono}")
    y -= 30

    for bitacora in bitacoras:
        if y < 120:
            dibujar_pie()
            p.showPage()
            dibujar_marca_agua()
            dibujar_encabezado()
            y = height - 80
        p.setFont("Montserrat-Bold", 12)
        p.setFillColor(verde_principal)
        p.drawString(50, y, f"Consulta: {bitacora.consulta.fecha} - Veterinario: {bitacora.veterinario.nombre if bitacora.veterinario else 'N/A'}")
        y -= 16
        p.setFont("Montserrat", 11)
        p.setFillColor(colors.black)
        p.drawString(60, y, f"Motivo: {bitacora.consulta.motivo}")
        y -= 14
        p.drawString(60, y, f"Diagnóstico: {bitacora.diagnostico}")
        y -= 14
        p.drawString(60, y, f"Tratamiento: {bitacora.tratamiento}")
        y -= 14
        medicamentos = ', '.join([m.nombre for m in bitacora.medicamentos.all()])
        p.drawString(60, y, f"Medicamentos: {medicamentos if medicamentos else 'Ninguno'}")
        y -= 14
        p.drawString(60, y, f"Observaciones: {bitacora.observaciones}")
        y -= 20
        p.setStrokeColor(verde_principal)
        p.line(50, y, width - 50, y)
        y -= 16

    dibujar_pie()
    p.save()
    return response