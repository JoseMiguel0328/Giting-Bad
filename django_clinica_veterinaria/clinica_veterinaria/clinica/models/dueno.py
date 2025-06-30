from django.db import models
from clinica_veterinaria.exceptions import DatoInvalidoError, TelefonoInvalidoError, DocumentoInvalidoError
from clinica_veterinaria.logging_config import get_logger

logger = get_logger('veterinaria')
error_logger = get_logger('veterinaria.errores')
acciones_logger = get_logger('clinica.acciones')

class Dueno(models.Model):
    documento = models.CharField(max_length=50, unique=True)
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=25)
    direccion = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Dueño"
        verbose_name_plural = "Dueños"
        ordering = ['nombre']
    
    def clean(self):
        """
        Validaciones personalizadas del modelo
        """
        super().clean()
        
        try:
            # Validar motivo
            if self.nombre:
                self.nombre = self._validar_cadena(self.nombre, "nombre")
            
            if self.documento:
                self.documento = self._validar_documento(self.documento)

            if self.telefono:
                self.telefono = self._validar_telefono(self.telefono)
            
            
        except (DatoInvalidoError, TelefonoInvalidoError, DocumentoInvalidoError) as e:
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
    
    def _validar_telefono(self, telefono):
        """
        Valida y normaliza teléfonos
        """
        telefono_str = str(telefono)
        if (not telefono_str.isdigit() or len(telefono_str) < 10):
            raise TelefonoInvalidoError("Número de teléfono inválido")
        return telefono_str
    
    def _validar_documento(self, documento):
        """
        Valida y normaliza documentos
        """
        documento_normalizado = str(documento.strip())
        if (not documento_normalizado.isdigit() or len(documento_normalizado) < 4):
            raise DocumentoInvalidoError("El documento es inválido.")
        return documento_normalizado
    
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
            accion = "cread@" if es_nueva else "actualizad@"
            logger.info(
                f"Dueñ@ {accion} exitosamente - ID: {self.id} - CC: {self.documento}"
            )
            acciones_logger.info(f"Dueño {'registrado' if es_nueva else 'editado'} - ID: {self.id}, Nombre: {self.nombre}")

        except Exception as e:
            error_logger.error(
                f"Error al guardar dueñ@: {str(e)}"
            )
            raise

    def delete(self, *args, **kwargs):
        acciones_logger.info(f"Dueño eliminado - ID: {self.id}, Nombre: {self.nombre}")
        super().delete(*args, **kwargs)

    def __str__(self):
        return f"{self.nombre}, Tel: {self.telefono}, Dir: {self.direccion}, CC: {self.documento}"