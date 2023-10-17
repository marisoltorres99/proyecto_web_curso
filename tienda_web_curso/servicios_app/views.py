from django.shortcuts import render

from servicios_app.models import Servicio


def servicios(request):

    servicios=Servicio.objects.all()
    return render(request, "servicios_app/servicios.html", {"servicios":servicios})
