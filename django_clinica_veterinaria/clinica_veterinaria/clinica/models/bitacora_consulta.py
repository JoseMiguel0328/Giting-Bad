from django.db import models
from .consulta import Consulta
from .mascota import Mascota
from .dueno import Dueno
from .veterinario import Veterinario
from .medicamento import Medicamento
from clinica_veterinaria.logging_config import get_logger

acciones_logger = get_logger('clinica.acciones')

class BitacoraConsulta(models.Model):
    consulta = models.OneToOneField(Consulta, on_delete=models.CASCADE, related_name='bitacora')
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE)
    dueno = models.ForeignKey(Dueno, on_delete=models.CASCADE)
    veterinario = models.ForeignKey(Veterinario, on_delete=models.SET_NULL, null=True)
    observaciones = models.TextField()
    diagnostico = models.TextField()
    tratamiento = models.TextField()
    medicamentos = models.ManyToManyField(Medicamento, blank=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Bitácora de {self.mascota.nombre} - {self.consulta.fecha}"

    def save(self, *args, **kwargs):
        es_nueva = self.pk is None
        super().save(*args, **kwargs)
        accion = "registrada" if es_nueva else "editada"
        acciones_logger.info(f"Bitácora {accion} - ID: {self.id}, Mascota: {self.mascota.nombre}, Consulta: {self.consulta.id}")

    def delete(self, *args, **kwargs):
        acciones_logger.info(f"Bitácora eliminada - ID: {self.id}, Mascota: {self.mascota.nombre}, Consulta: {self.consulta.id}")
        super().delete(*args, **kwargs)