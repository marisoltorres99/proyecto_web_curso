from django.shortcuts import HttpResponse, render


def home(request):
    return render(request, "proyecto_web_app/home.html")

def tienda(request):
    return render(request, "proyecto_web_app/tienda.html")

def contacto(request):
    return render(request, "proyecto_web_app/contacto.html")
