from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


def hello_world(request):
    return HttpResponse("Hello World")

class hello_colombia(View):
    def get(self, request):
        return HttpResponse("Hello Colombia")
    
def landing_page(request):
    return render(request, 'clinica/index.html')

def services(request):
    return render(request, 'clinica/services.html')

