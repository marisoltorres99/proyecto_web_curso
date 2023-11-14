from django.shortcuts import redirect, render
from tienda_app.models import Producto

from .carro import Carro


def agregar_producto(request, producto_id):
    carro = Carro(request)

    producto = Producto.objects.get(id=producto_id)

    carro.agregar(producto=producto)

    return redirect("Tienda")


def eliminar_producto(request, producto_id):
    carro = Carro(request)

    producto = Producto.objects.get(id=producto_id)

    carro.eliminar(producto=producto)

    return redirect("Tienda")


def restar_producto(request, producto_id):
    carro = Carro(request)

    producto = Producto.objects.get(id=producto_id)

    carro.restar(producto=producto)

    return redirect("Tienda")


def limpiar_carro(request):
    carro = Carro(request)

    carro.limpiar()

    return redirect("Tienda")
