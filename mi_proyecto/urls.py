from django.contrib import admin
from django.urls import path, include
from productos import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.catalogo, name='catalogo'),
    path('producto/<int:id>/', views.detalle_producto, name='detalle_producto'),
    path('carrito/', views.ver_carrito, name='ver_carrito'),
    path('agregar/<int:id>/', views.agregar_carrito, name='agregar_carrito'),
    path('quitar/<int:id>/', views.quitar_carrito, name='quitar_carrito'),
    path('actualizar/<int:id>/', views.actualizar_cantidad, name='actualizar_cantidad'),
    path('confirmar/', views.confirmar_compra, name='confirmar_compra'),
    path('accounts/', include('django.contrib.auth.urls')),
]