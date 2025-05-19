"""
---- Información ----
En este archivo se define la clase Consulta, que representa una consulta médica hecha a una mascota.
Valida los datos ingresados y deja registro en los logs del sistema para control y depuración.
"""
from config.logging_config import logger
from datetime import datetime

class Consulta():
    def __init__(self, fecha='', motivo='', diagnostico='', mascota=''):
        """
        1. El constructor recibe la fecha, el motivo, el diagnóstico y la mascota relacionada.
        2. Valida que la fecha esté en formato correcto (dd/mm/yyyy).
        3. Valida que el motivo y el diagnóstico no estén vacíos.
        4. Si todo es válido, asigna los valores a los atributos.
        5. Deja registro en el log de que la consulta fue registrada exitosamente.
        6. Si hay algún error en los datos, se deja registro en el log del error.
        """
        try:
            #2
            self.fecha = self._validar_fecha(fecha)
            #3
            self.motivo = self._validar_cadena(motivo)
            self.diagnostico = self._validar_cadena(diagnostico)
            #4
            self.mascota = mascota
            #5
            logger.info("La consulta se ha registrado correctamente.")
        #6
        except Exception as e:
            logger.error(f"Ha ocurrido un error al registrar la consulta: {e}")
            raise

    def _validar_cadena(self, argumento):
        """
        1. Normaliza el texto (capitaliza y elimina espacios).
        2. Verifica que no esté vacío ni contenga solo espacios.
        3. Si no es válido, lanza un error.
        4. Si es válido, lo retorna.
        """
        argumento_normalizado = argumento.capitalize().strip()
        if (not argumento_normalizado or argumento_normalizado.isspace()):
            raise ValueError("El argumento no puede estar vacío.")
        return argumento_normalizado

    def _validar_fecha(self, fecha):
        """
        1. Intenta convertir el texto recibido a un objeto datetime con formato día/mes/año.
        2. Si el formato no es válido, registra el error en el log.
        3. Si es válido, retorna el objeto datetime.
        """
        try:
            fecha_normalizada = datetime.strptime(fecha.strip(), "%d/%m/%Y")
            return fecha_normalizada
        except ValueError as e:
            logger.error(f"Fecha inválida ingresada: '{fecha}' -> {e}")
            raise ValueError(f"Formato de fecha inválido. Use dd/mm/aaaa.")

    def __str__(self):
        """
        Método especial que retorna una representación legible de la consulta.
        Se puede usar, por ejemplo, al imprimir el objeto en consola.
        """
        return f"Fecha: {self.fecha}, Motivo: {self.motivo}, Diagnóstico: {self.diagnostico}"