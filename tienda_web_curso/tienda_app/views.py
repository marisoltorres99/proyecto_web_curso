from django.shortcuts import render


def tienda(request):
    return render(request, "tienda_app/tienda.html")
