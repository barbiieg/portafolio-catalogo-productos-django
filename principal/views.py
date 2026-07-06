from django.shortcuts import render, redirect
from .forms import ContactoModelForm

def contacto(request):
    if request.method == "POST":
        formulario = ContactoModelForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect("exito")
    else:
        formulario = ContactoModelForm()

    return render(request, "contacto.html", {"form": formulario})

def exito(request):
    return render(request, "exito.html")