# veterinaria/exceptions/errores.py
"""
Excepciones personalizadas para la aplicación veterinaria.
"""

from django.core.exceptions import ValidationError


class BaseError(Exception):
    """
    Excepción base para todas las excepciones personalizadas de la aplicación.
    """
    def __init__(self, message="Error en la aplicación veterinaria"):
        self.message = message
        super().__init__(self.message)


class DatoInvalidoError(ValidationError, BaseError):
    """
    Excepción para datos inválidos en los modelos.
    Hereda de ValidationError para compatibilidad con Django.
    """
    def __init__(self, message="Dato inválido proporcionado"):
        BaseError.__init__(self, message)
        ValidationError.__init__(self, message)

class TelefonoInvalidoError(BaseError):
    def __init__(self, mensaje="Debe ingresar un teléfono permitido."):
        super().__init__(mensaje)
    pass

class DocumentoInvalidoError(BaseError):
    def __init__(self, mensaje="Debe ingresar un documento valido."):
        super().__init__(mensaje)
    pass

class EdadInvalidaError(BaseError):
    def __init__(self, mensaje="Debe ingresar una edad permitida."):
        super().__init__(mensaje)
    pass

class FechaInvalidaError(ValidationError, BaseError):
    """
    Excepción específica para errores de formato de fecha.
    """
    def __init__(self, message="Formato de fecha inválido"):
        BaseError.__init__(self, message)
        ValidationError.__init__(self, message)


class MascotaNoEncontradaError(BaseError):
    """
    Excepción cuando no se encuentra una mascota.
    """
    def __init__(self, message="Mascota no encontrada"):
        super().__init__(message)


class DuenoNoEncontradoError(BaseError):
    """
    Excepción cuando no se encuentra un dueño.
    """
    def __init__(self, message="Dueño no encontrado"):
        super().__init__(message)


class ConsultaDuplicadaError(BaseError):
    """
    Excepción para consultas duplicadas.
    """
    def __init__(self, message="Ya existe una consulta similar"):
        super().__init__(message)


class PermisosDenegadosError(BaseError):
    """
    Excepción para problemas de permisos.
    """
    def __init__(self, message="No tiene permisos para realizar esta acción"):
        super().__init__(message)

