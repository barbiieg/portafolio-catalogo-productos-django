from django.contrib import admin
from django.urls import path, include  
from principal import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.contacto, name="contacto"),
    path("exito/", views.exito, name="exito"),
    path("libros/", include("libros.urls")),
       path("products/", include("productos.urls")),
]