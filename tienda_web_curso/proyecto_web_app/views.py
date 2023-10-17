from django.shortcuts import HttpResponse, render
from servicios_app.models import Servicio


def home(request):
    return render(request, "proyecto_web_app/home.html")

def servicios(request):

    servicios=Servicio.objects.all()
    return render(request, "proyecto_web_app/servicios.html", {"servicios":servicios})

def tienda(request):
    return render(request, "proyecto_web_app/tienda.html")

def blog(request):
    return render(request, "proyecto_web_app/blog.html")

def contacto(request):
    return render(request, "proyecto_web_app/contacto.html")
