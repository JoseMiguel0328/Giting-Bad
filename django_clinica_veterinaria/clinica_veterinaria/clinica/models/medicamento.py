from django.db import models
from clinica_veterinaria.logging_config import get_logger
from django.utils import timezone
from clinica_veterinaria.exceptions import DatoInvalidoError

logger = get_logger('veterinaria')
error_logger = get_logger('veterinaria.errores')
acciones_logger = get_logger('clinica.acciones')

class Medicamento(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    cantidad_disponible = models.PositiveIntegerField()
    fecha_vencimiento = models.DateField()

    class Meta:
        verbose_name = "Medicamento"
        verbose_name_plural = "Medicamentos"
        ordering = ['nombre']

    def clean(self):
        try:
            if self.nombre:
                self.nombre = self._validar_cadena(self.nombre, "nombre")
            if self.descripcion:
                self.descripcion = self._validar_cadena(self.descripcion, "descripción")
        except DatoInvalidoError as e:
            error_logger.error(f"Error de validación en medicamento: {str(e)}")
            raise

    def _validar_cadena(self, argumento, campo):
        if not argumento:
            return argumento
        argumento_normalizado = argumento.strip().title()
        if not argumento_normalizado or argumento_normalizado.isspace():
            raise DatoInvalidoError(f"El campo {campo} no puede estar vacío.")
        return argumento_normalizado

    def save(self, *args, **kwargs):
        es_nuevo = self.pk is None
        super().save(*args, **kwargs)
        accion = "registrado" if es_nuevo else "editado"
        acciones_logger.info(f"Medicamento {accion} - ID: {self.id}, Nombre: {self.nombre}")

    def delete(self, *args, **kwargs):
        acciones_logger.info(f"Medicamento eliminado - ID: {self.id}, Nombre: {self.nombre}")
        super().delete(*args, **kwargs)

    def esta_vencido(self):
        return self.fecha_vencimiento < timezone.now().date()

    def esta_bajo_stock(self):
        return self.cantidad_disponible <= 5

    def __str__(self):
        return f"{self.nombre} - {self.cantidad_disponible} unidades (vence: {self.fecha_vencimiento})"