from django.db import models
from clinica_veterinaria.logging_config import get_logger
from clinica_veterinaria.exceptions import DatoInvalidoError
from django.contrib.auth.models import User

logger = get_logger('veterinaria')
error_logger = get_logger('veterinaria.errores')
acciones_logger = get_logger('clinica.acciones')

class Veterinario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    nombre = models.CharField(max_length=100)
    documento = models.CharField(max_length=20, unique=True)
    telefono = models.CharField(max_length=15)
    especialidad = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Veterinario"
        verbose_name_plural = "Veterinarios"
        ordering = ['nombre']

    def clean(self):
        super().clean()
        try:
            self.nombre = self._validar_campo(self.nombre, "nombre")
            self.telefono = self._validar_campo(self.telefono, "teléfono")
            self.especialidad = self._validar_campo(self.especialidad, "especialidad")
        except DatoInvalidoError as e:
            error_logger.error(f"Error al validar veterinario: {str(e)}")
            raise

    def _validar_campo(self, valor, campo):
        if not valor or valor.strip() == "":
            raise DatoInvalidoError(f"El campo {campo} no puede estar vacío.")
        return valor.title().strip()

    def save(self, *args, **kwargs):
        es_nuevo = self.pk is None
        super().save(*args, **kwargs)
        accion = "registrado" if es_nuevo else "editado"
        acciones_logger.info(f"Veterinario {accion} - ID: {self.id}, Nombre: {self.nombre}")

    def delete(self, *args, **kwargs):
        acciones_logger.info(f"Veterinario eliminado - ID: {self.id}, Nombre: {self.nombre}")
        super().delete(*args, **kwargs)

    def __str__(self):
        return f"{self.nombre} ({self.especialidad}) - Tel: {self.telefono}, Doc: {self.documento}"