from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Producto, Pedido, ItemPedido

def catalogo(request):
    productos = Producto.objects.all()
    return render(request, 'catalogo.html', {'productos': productos})

def detalle_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    return render(request, 'detalle.html', {'producto': producto})

def ver_carrito(request):
    carrito = request.session.get('carrito', {})
    items = []
    total = 0
    for prod_id, cantidad in carrito.items():
        p = get_object_or_404(Producto, id=prod_id)
        subtotal = p.precio * cantidad
        items.append({'producto': p, 'cantidad': cantidad, 'subtotal': subtotal})
        total += subtotal
    return render(request, 'carrito.html', {'items': items, 'total': total})

def agregar_carrito(request, id):
    carrito = request.session.get('carrito', {})
    carrito[str(id)] = carrito.get(str(id), 0) + 1
    request.session['carrito'] = carrito
    messages.success(request, '✅ Producto agregado al carrito')
    return redirect('catalogo')

def quitar_carrito(request, id):
    carrito = request.session.get('carrito', {})
    if str(id) in carrito:
        del carrito[str(id)]
        request.session['carrito'] = carrito
    messages.info(request, '🗑️ Producto eliminado del carrito')
    return redirect('ver_carrito')

def actualizar_cantidad(request, id):
    if request.method == 'POST':
        cantidad = int(request.POST.get('cantidad', 1))
        if cantidad > 0:
            carrito = request.session.get('carrito', {})
            carrito[str(id)] = cantidad
            request.session['carrito'] = carrito
            messages.success(request, '🔄 Cantidad actualizada')
    return redirect('ver_carrito')

@login_required
def confirmar_compra(request):
    carrito = request.session.get('carrito', {})
    if not carrito:
        messages.warning(request, '⚠️ El carrito está vacío')
        return redirect('catalogo')
    pedido = Pedido(usuario=request.user)
    pedido.save()
    total_final = 0
    for prod_id, cantidad in carrito.items():
        p = get_object_or_404(Producto, id=prod_id)
        subtotal = p.precio * cantidad
        ItemPedido(pedido=pedido, producto=p, cantidad=cantidad, subtotal=subtotal).save()
        total_final += subtotal
    pedido.total = total_final
    pedido.save()
    del request.session['carrito']
    messages.success(request, '🎉 Compra realizada con éxito')
    return redirect('catalogo')