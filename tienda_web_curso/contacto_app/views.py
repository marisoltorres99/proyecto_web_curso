from django.shortcuts import redirect, render

from contacto_app.forms import FormularioContacto


def contacto(request):
    formulario_contacto = FormularioContacto()
    if request.method == "POST":
        formulario_contacto = FormularioContacto(request.POST)
        if formulario_contacto.is_valid():
            nombre = request.POST.get("nombre")
            email = request.POST.get("email")
            contenido = request.POST.get("contenido")
            return redirect("/contacto/?valido")

    return render(request, "contacto_app/contacto.html", {"form": formulario_contacto})
