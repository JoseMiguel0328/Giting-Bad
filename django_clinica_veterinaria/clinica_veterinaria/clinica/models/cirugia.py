from django.db import models
from clinica.models.mascota import Mascota
from clinica.models.veterinario import Veterinario
from clinica_veterinaria.logging_config import get_logger
from clinica_veterinaria.exceptions import DatoInvalidoError

logger = get_logger('veterinaria')
error_logger = get_logger('veterinaria.errores')
acciones_logger = get_logger('clinica.acciones')

class Cirugia(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha = models.DateField()
    mascota = models.ForeignKey(Mascota, on_delete=models.PROTECT, related_name='cirugias')
    veterinario = models.ForeignKey(Veterinario, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = "Cirugía"
        verbose_name_plural = "Cirugías"
        ordering = ['fecha']

    def clean(self):
        super().clean()
        try:
            if self.nombre:
                self.nombre = self._validar_cadena(self.nombre, "nombre")
            if self.descripcion:
                self.descripcion = self._validar_cadena(self.descripcion, "descripción")
            if self.mascota is None:
                raise DatoInvalidoError("Debe asociarse una mascota a la cirugía.")
        except DatoInvalidoError as e:
            error_logger.error(f"Error de validación en cirugía: {str(e)}")
            raise

    def _validar_cadena(self, argumento, campo):
        if not argumento:
            return argumento
        argumento_normalizado = argumento.strip().capitalize()
        if not argumento_normalizado or argumento_normalizado.isspace():
            raise DatoInvalidoError(f"El campo {campo} no puede estar vacío.")
        return argumento_normalizado

    def save(self, *args, **kwargs):
        es_nueva = self.pk is None
        super().save(*args, **kwargs)
        accion = "registrada" if es_nueva else "editada"
        acciones_logger.info(f"Cirugía {accion} - ID: {self.id}, Nombre: {self.nombre}")
        try:
            self.full_clean()
            es_nueva = self.pk is None
            super().save(*args, **kwargs)
            accion = "creada" if es_nueva else "actualizada"
            logger.info(f"Cirugía {accion} correctamente - ID: {self.id}")
        except Exception as e:
            error_logger.error(f"Error al guardar cirugía: {str(e)}")
            raise

    def delete(self, *args, **kwargs):
        acciones_logger.info(f"Cirugía eliminada - ID: {self.id}, Nombre: {self.nombre}")
        super().delete(*args, **kwargs)

    def __str__(self):
        veterinario_nombre = self.veterinario.get_full_name() if self.veterinario else "No asignado"
        return (f"Cirugía: {self.nombre} ({self.fecha})\n"
            f"Mascota: {self.mascota.nombre} - Dueño: {self.mascota.dueno.nombre}\n"
            f"Veterinario: {veterinario_nombre}")