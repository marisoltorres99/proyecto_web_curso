from django.shortcuts import render


def contacto(request):
    return render(request, "contacto_app/contacto.html")
