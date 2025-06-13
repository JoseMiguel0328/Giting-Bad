"""

---- Información ----
En este archivo se define la clase Consulta, que representa una consulta médica hecha a una mascota.
Valida los datos ingresados y deja registro en los logs del sistema para control y depuración.
"""
from config.logging_config import logger
from datetime import datetime
from exceptions.errores import DatoInvalidoError, FechaInvalidaError
from services.db import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text

class Consulta(Base):

    __tablename__='consultas'
    id = Column(Integer, primary_key=True, autoincrement=True)
    fecha = Column(DateTime, default=datetime.now)
    motivo = Column(String(255), nullable=False)
    diagnostico = Column(Text)

    mascota_id = Column(Integer, ForeignKey('mascotas.id'), nullable=False)
    mascota = relationship("Mascota", back_populates="consultas")


    def __init__(self, fecha='', motivo='', diagnostico='', mascota=''):
        """
        1. El constructor recibe la fecha, el motivo, el diagnóstico y la mascota relacionada.
        2. Valida que la fecha esté en formato correcto (dd/mm/yyyy).
        3. Valida que el motivo y el diagnóstico no estén vacíos.
        4. Si todo es válido, asigna los valores a los atributos.
        5. Deja registro en el log de que la consulta fue registrada exitosamente.
        """
        #2
        super().__init__()
        self.fecha = self._validar_fecha(fecha)
        #3
        self.motivo = self._validar_cadena(motivo, "motivo")
        self.diagnostico = self._validar_cadena(diagnostico, "diagnóstico")
        #4
        self.mascota = mascota
        #5
        logger.info("La consulta se ha registrado correctamente.")

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

    def _validar_fecha(self, fecha):
        """
        1. Intenta convertir el texto recibido a un objeto datetime con formato día/mes/año.
        2. Si el formato no es válido, registra el error en el log.
        3. Si es válido, retorna el objeto datetime.
        """
        try:
            fecha_normalizada = datetime.strptime(fecha.strip(), "%d/%m/%Y")
            return fecha_normalizada
        except ValueError:
            raise FechaInvalidaError(f"Formato de fecha inválido. Use dd/mm/aaaa.")

    def __str__(self):
        """
        Método especial que retorna una representación legible de la consulta.
        Se puede usar, por ejemplo, al imprimir el objeto en consola.
        """
        return f"Fecha: {self.fecha}, Motivo: {self.motivo}, Diagnóstico: {self.diagnostico}"

