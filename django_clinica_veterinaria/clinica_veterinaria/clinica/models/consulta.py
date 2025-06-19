from django.db import models
from clinica_veterinaria.exceptions import DatoInvalidoError, FechaInvalidaError
from datetime import date
from clinica_veterinaria.logging_config import get_logger
from .mascota import Mascota

logger = get_logger('veterinaria')
error_logger = get_logger('veterinaria.errores')


class Consulta(models.Model):
    fecha = models.DateField()
    motivo = models.TextField()
    diagnostico = models.TextField()

    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE, related_name='consultas')

    class Meta:
        verbose_name = "Consulta"
        verbose_name_plural = "Consultas"
        ordering = ['-fecha']

    def clean(self):
        """
        Validaciones personalizadas del modelo
        """
        super().clean()
        
        try:
            # Validar motivo
            if self.motivo:
                self.motivo = self._validar_cadena(self.motivo, "motivo")
            
            # Validar diagnóstico
            if self.diagnostico:
                self.diagnostico = self._validar_cadena(self.diagnostico, "diagnóstico")
            
            # Validar que la fecha no sea futura
            if self.fecha and self.fecha > date.today():
                raise FechaInvalidaError("La fecha de consulta no puede ser futura.")
        
        except (DatoInvalidoError, FechaInvalidaError) as e:
            error_logger.error(f"Error de validación en consulta: {str(e)}")
            raise

    def _validar_cadena(self, argumento, campo):
        """
        Valida y normaliza cadenas de texto
        """
        if not argumento:
            return argumento
        
        argumento_normalizado = argumento.title().strip()
        if not argumento_normalizado or argumento_normalizado.isspace():
            raise DatoInvalidoError(f"El campo {campo} no puede estar vacío.")
        
        return argumento_normalizado
    
    def save(self, *args, **kwargs):
        """
        Override del método save para logging
        """
        try:
            # Validar antes de guardar
            self.full_clean()
            
            # Determinar si es creación o actualización
            es_nueva = self.pk is None
            
            # Guardar el objeto
            super().save(*args, **kwargs)
            
            # Log exitoso
            accion = "creada" if es_nueva else "actualizada"
            logger.info(
                f"Consulta {accion} exitosamente - ID: {self.id}, "
                f"Mascota: {self.mascota.nombre}, Fecha: {self.fecha}"
            )

        except Exception as e:
            error_logger.error(
                f"Error al guardar consulta - Mascota: {getattr(self.mascota, 'nombre', 'N/A')}, "
                f"Error: {str(e)}"
            )
            raise

    def __str__(self):
        return f"Fecha: {self.fecha} \nMotivo: {self.motivo} \nDiagnóstico: {self.diagnostico}"
