from django.shortcuts import HttpResponse, render


def home(request):
    return render(request, "proyecto_web_app/home.html")
