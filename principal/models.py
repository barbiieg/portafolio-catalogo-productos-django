from django.db import models

class ConsultaContacto(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    mensaje = models.TextField()
    fecha_envio = models.DateTimeField(auto_now_add=True)
    # Campo nuevo agregado para la actividad
    asunto = models.CharField(max_length=80, null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} - {self.fecha_envio.strftime('%d/%m/%Y')}"