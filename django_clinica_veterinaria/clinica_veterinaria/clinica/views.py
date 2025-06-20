from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.views import View
from .models.mascota import Mascota
from .forms.mascota_form import MascotaForm
from .models import Dueno
from .forms import DuenoForm
from .models import Consulta
from .forms import ConsultaForm



def hello_world(request):
    return HttpResponse("Hello World")

class hello_colombia(View):
    def get(self, request):
        return HttpResponse("Hello Colombia")
    
def landing_page(request):
    return render(request, 'clinica/index.html')

def services(request):
    return render(request, 'clinica/services.html')

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
    tiene_mascotas = dueno.mascotas.exists() 

    if request.method == 'POST' and not tiene_mascotas:
        dueno.delete()
        return redirect('gestionar_duenos')
    return render(request, 'clinica/eliminar_dueno.html', {
        'dueno': dueno,
        'tiene_mascotas': tiene_mascotas
    })

def gestionar_citas(request):
    citas = Consulta.objects.all()
    return render(request, 'clinica/citas.html', {'citas': citas})

def crear_cita(request):
    if request.method == 'POST':
        form = ConsultaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gestionar_citas')
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
