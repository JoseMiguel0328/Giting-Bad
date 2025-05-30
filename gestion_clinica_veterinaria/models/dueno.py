"""
---- Información ----
En este archivo se define la clase Dueno, que representa al dueño de una mascota registrada.
Se validan los datos básicos del dueño y se registran los procesos importantes mediante el logger.

"""
import csv
from config.logging_config import logger
from exceptions.errores import DatoInvalidoError, TelefonoInvalidoError, DocumentoInvalidoError

class Dueno():
    def __init__(self, nombre='', telefono='', direccion='', documento=''):
        """
        1. El constructor recibe la información del dueño.
        2. Se valida que el nombre y la dirección no estén vacíos.
        3. Se valida que el teléfono tenga al menos 10 dígitos y sea numérico.
        4. Se valida que el documento tenga al menos 4 dígitos y sea numérico.
        5. Si todo es correcto, se asignan los valores como atributos.
        6. Se deja registro en el log de que el dueño fue registrado exitosamente.
        """
        #2
        self.nombre = self._validar_cadena(nombre, "nombre")
        #3
        self.telefono = self._validar_telefono(telefono)
        #2
        self.direccion = self._validar_cadena(direccion, "dirección")
        #4
        self.documento = self._validar_documento(documento)
        #6
        logger.info(f"Se ha registrado exitosamente el dueño {self.nombre}")

    def _validar_telefono(self, telefono):
        """
        1. Convierte el teléfono a string.
        2. Verifica que tenga al menos 10 dígitos y sea numérico.
        3. Si no cumple, lanza un error.
        4. Si cumple, retorna el número como string.
        """
        telefono_str = str(telefono)
        if (not telefono_str.isdigit() or len(telefono_str) < 10):
            raise TelefonoInvalidoError("Número de teléfono inválido")
        return telefono_str

    def _validar_cadena(self, argumento, campo):
        """
        1. Normaliza el texto (capitaliza y elimina espacios).
        2. Verifica que no esté vacío ni contenga solo espacios.
        3. Si no es válido, lanza un error.
        4. Si es válido, lo retorna.
        """
        argumento_normalizado = argumento.capitalize().strip()
        if (not argumento_normalizado or argumento_normalizado.isspace()):
            raise DatoInvalidoError(f"El argumento {campo} no puede estar vacío.")
        return argumento_normalizado

    def _validar_documento(self, documento):
        """
        1. Normaliza el documento quitando espacios.
        2. Verifica que sea numérico y tenga al menos 4 dígitos.
        3. Si no cumple, lanza un error.
        4. Si cumple, lo retorna como string.
        """
        documento_normalizado = str(documento.strip())
        if (not documento_normalizado.isdigit() or len(documento_normalizado) < 4):
            raise DocumentoInvalidoError("El documento es inválido.")
        return documento_normalizado

