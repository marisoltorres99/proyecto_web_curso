from django.shortcuts import render

from contacto_app.forms import FormularioContacto


def contacto(request):
    formulario_contacto = FormularioContacto()
    return render(request, "contacto_app/contacto.html", {"form": formulario_contacto})
