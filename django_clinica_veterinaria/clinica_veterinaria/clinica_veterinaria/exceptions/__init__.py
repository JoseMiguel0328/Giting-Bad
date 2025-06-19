"""
Módulo de excepciones personalizadas para la aplicación veterinaria.
"""

from .errores import (
    BaseError,
    TelefonoInvalidoError,
    DocumentoInvalidoError,
    DatoInvalidoError,
    EdadInvalidaError,
    FechaInvalidaError,
    MascotaNoEncontradaError,
    DuenoNoEncontradoError,
    ConsultaDuplicadaError,
    PermisosDenegadosError,
)

__all__ = [
    'BaseError',
    'TelefonoInvalidoError',
    'DocumentoInvalidoError',
    'EdadInvalidaError',
    'DatoInvalidoError',
    'FechaInvalidaError',
    'MascotaNoEncontradaError',
    'DuenoNoEncontradoError',
    'ConsultaDuplicadaError',
    'PermisosDenegadosError',
]