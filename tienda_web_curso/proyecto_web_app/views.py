from carro_app.carro import Carro
from django.shortcuts import HttpResponse, render


def home(request):
    carro = Carro(request)
    return render(request, "proyecto_web_app/home.html")
