from django import forms

# Formulario básico como muestra la guía
class ContactoForm(forms.Form):
    nombre = forms.CharField(max_length=100, label="Nombre completo")
    correo = forms.EmailField(label="Correo electrónico")
    mensaje = forms.CharField(
        widget=forms.Textarea,
        min_length=10,
        label="Escribe tu mensaje"
    )

# Versión ModelForm (punto opcional)
from .models import ConsultaContacto
class ContactoModelForm(forms.ModelForm):
    class Meta:
        model = ConsultaContacto
        fields = ["nombre", "correo", "mensaje"]
        labels = {
            "nombre": "Nombre completo",
            "correo": "Correo electrónico",
            "mensaje": "Escribe tu mensaje"
        }