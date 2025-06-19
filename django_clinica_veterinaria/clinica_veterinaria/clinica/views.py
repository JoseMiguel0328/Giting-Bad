from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .models import Mascota
from .forms import MascotaForm


def hello_world(request):
    return HttpResponse("Hello World")

class hello_colombia(View):
    def get(self, request):
        return HttpResponse("Hello Colombia")
    
def landing_page(request):
    return render(request, 'clinica/index.html')

def services(request):
    return render(request, 'clinica/services.html')

def listar_mascotas(request):
    mascotas = Mascota.objects.select_related("dueno").all()
    return render(request, "clinica/listar_mascotas.html", {"mascotas": mascotas})

def crear_mascota(request):
    if request.method == 'POST':
        form = MascotaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_mascotas')
    else:
        form = MascotaForm()
    return render(request, 'clinica/crear_mascota.html', {'form': form})
