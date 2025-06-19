from django.db import models
from clinica_veterinaria.exceptions import DatoInvalidoError, EdadInvalidaError
from clinica_veterinaria.logging_config import get_logger
from .dueno import Dueno

logger = get_logger('veterinaria')
error_logger = get_logger('veterinaria.errores')

class Mascota(models.Model):
    nombre = models.CharField(max_length=100)
    especie = models.CharField(max_length=50)
    raza = models.CharField(max_length=50)
    edad = models.IntegerField()
    dueno = models.ForeignKey(Dueno, on_delete=models.PROTECT, to_field='documento', related_name='mascotas')

    class Meta:
        verbose_name = "Mascota"
        verbose_name_plural = "Mascotas"
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

            if self.edad:
                self.edad = self._validar_edad(self.edad)

            if self.dueno:
                self.dueno = self._validar_dueno(self.dueno)

        except (DatoInvalidoError, EdadInvalidaError) as e:
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
    
    def _validar_edad(self, edad):
        """
        1. Convierte la edad a cadena.
        2. Verifica que sea un número entero válido.
        3. Si no lo es o es negativo, lanza un error.
        4. Si es válida, devuelve la edad como entero.
        """
        edad_str = str(edad)
        if (not edad_str.isdigit()):
            raise EdadInvalidaError("La edad debe ser un número entero.")
        edad_int = int(edad_str)
        if (edad_int < 0):
            raise EdadInvalidaError("Edad no permitida.")
        return edad_int

    def _validar_dueno(self, dueno):
        if dueno is None:
            raise DatoInvalidoError("El dueño no puede estar vacío.")
        if not isinstance(dueno, Dueno):
            raise DatoInvalidoError("El dueño debe ser un objeto válido de la clase Dueno.")
        return dueno
    
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
                f"Mascota {accion} exitosamente - ID: {self.id}"
            )

        except Exception as e:
            error_logger.error(
                f"Error al guardar mascota: {str(e)}"
            )
            raise

    def __str__(self):
        return f"{self.nombre} ({self.especie}, {self.raza}, {self.edad} años) \n  Dueño: {self.dueno.nombre} Tel: {self.dueno.telefono}, Dir: {self.dueno.direccion}, CC:{self.dueno.documento}"
