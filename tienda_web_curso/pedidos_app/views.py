from carro_app.carro import Carro
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from pedidos_app.models import LineaPedido, Pedido


@login_required(login_url="/autenticacion_app/iniciar_sesion")
def procesar_pedido(request):
    pedido = Pedido.objects.create(user=request.user)
    carro = Carro(request)
    lineas_pedido = list()

    for key, value in carro.carro.items():
        lineas_pedido.append(
            LineaPedido(
                producto_id=key,
                cantidad=value["cantidad"],
                user=request.user,
                pedido=pedido,
            )
        )

    LineaPedido.objects.bulk_create(lineas_pedido)

    messages.success(request, "El pedido se ha creaco correctamente")

    return redirect("/tienda")
