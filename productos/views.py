from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Producto
from .forms import ProductoForm

# Listar todos los productos
def listar_productos(request):
    productos = Producto.objects.all().select_related('categoria')
    return render(request, 'listar_productos.html', {'productos': productos})

# Crear producto
def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ Producto guardado correctamente")
            return redirect('listar_productos')  # ← AQUÍ te debe llevar a la lista
        else:
            messages.error(request, "❌ Revisa los datos: precio > 0, categoría seleccionada")
    else:
        form = ProductoForm()
    return render(request, 'formulario_producto.html', {'form': form, 'accion': 'Crear'})

# Editar producto
def editar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ Producto actualizado")
            return redirect('listar_productos')
        else:
            messages.error(request, "❌ Revisa los datos")
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'formulario_producto.html', {'form': form, 'accion': 'Editar'})

# Eliminar producto
def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        producto.delete()
        messages.success(request, "✅ Producto eliminado")
        return redirect('listar_productos')
    return render(request, 'confirmar_eliminacion.html', {'producto': producto})