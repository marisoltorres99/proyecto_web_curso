from django.shortcuts import render


def autenticacion(request):
    return render(request, "registro/registro.html")
