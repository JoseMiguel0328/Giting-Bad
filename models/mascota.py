"""
---- Información ----
En este archivo se define la clase Mascota, que representa una mascota registrada en la veterinaria.
Esta clase incluye validaciones básicas para garantizar que los datos ingresados sean correctos.
Además, se utiliza el logger para registrar el estado de la creación de objetos y errores.
"""

from config.logging_config import logger
from exceptions.errores import DatoInvalidoError, EdadInvalidaError

class Mascota():
    def __init__(self, nombre='', especie='', raza='', edad='', dueno=''):
        """
        1. El constructor recibe los datos de la mascota.
        2. Se valida que nombre, especie y raza sean cadenas no vacías.
        3. Se valida que la edad sea un número entero válido.
        4. Se asigna el objeto dueño a la mascota.
        5. Se registra en el log que la mascota fue creada exitosamente.
        """
        #2
        self.nombre = self._validar_cadena(nombre, "nombre")
        self.especie = self._validar_cadena(especie, "especie")
        self.raza = self._validar_cadena(raza, "raza")
        #3
        self.edad = self._validar_edad(edad)
        #4
        self.dueno = dueno
        #5
        logger.info(f"La mascota {self.nombre} se ha creado exitosamente.")
        

    def _validar_cadena(self, argumento, campo):
        """
        1. Normaliza la cadena (capitaliza y quita espacios).
        2. Verifica que no esté vacía ni contenga solo espacios.
        3. Si no es válida, lanza un error.
        4. Si es válida, la devuelve.
        """
        argumento_normalizado = argumento.capitalize().strip()
        if (not argumento_normalizado or argumento_normalizado.isspace()):
            raise DatoInvalidoError(f"El argumento {campo} no puede estar vacío.")
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

    def __str__(self):
        """
        1. Método especial que retorna una representación en texto del objeto mascota.
        2. Incluye información de la mascota y su dueño.
        """
        return f"{self.nombre} ({self.especie}, {self.raza}, {self.edad} años) \n  Dueño: {self.dueno.nombre} Tel: {self.dueno.telefono}, Dir: {self.dueno.direccion}, CC:{self.dueno.documento}"
