from django.shortcuts import HttpResponse, render


def home(request):
    return HttpResponse("Home")

def servicios(request):
    return HttpResponse("Servicios")

def tienda(request):
    return HttpResponse("Tienda")

def blog(request):
    return HttpResponse("Blog")

def contacto(request):
    return HttpResponse("Contacto")
