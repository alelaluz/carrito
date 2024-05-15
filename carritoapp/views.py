from django.shortcuts import render, HttpResponse, redirect
from carritoapp.models import Producto
from carritoapp.Carrito import Carrito
# Create your views here.


def tienda(request):
    # para probar la pagina
    # return HttpResponse("hola amigos")
    productos = Producto.objects.all()
    return render(request, "tienda.html", {'productos': productos})


def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.agregar(producto)
    return redirect("Tienda")


def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.elimninar(producto)
    return redirect("Tienda")


def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect("Tienda")


def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("Tienda")
