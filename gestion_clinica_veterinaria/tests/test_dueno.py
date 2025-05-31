import unittest
from models.dueno import Dueno
from exceptions.errores import TelefonoInvalidoError, DatoInvalidoError

class TestDueno(unittest.TestCase):
    """
    Clase de pruebas unitarias para la clase Dueno.

    Pruebas:
        - test_creacion_exitosa: Verifica que un dueño se cree correctamente con datos válidos.
        - test_telefono_invalido: Verifica que se lance TelefonoInvalidoError cuando el teléfono es inválido.
        - test_nombre_vacio: Verifica que se lance DatoInvalidoError cuando el nombre está vacío o solo contiene espacios.
    """

    def test_creacion_exitosa(self):
        """
        Prueba la creación exitosa de un objeto Dueno con datos válidos.
        Comprueba que los atributos nombre y teléfono se asignen correctamente.
        """
        dueno = Dueno(nombre="Carlos", telefono="3101234567", direccion="Calle 1", documento="1234567890")
        self.assertEqual(dueno.nombre, "Carlos")
        self.assertEqual(dueno.telefono, "3101234567")

    def test_telefono_invalido(self):
        """
        Prueba que la creación de un Dueno con un teléfono inválido
        lance la excepción TelefonoInvalidoError.
        """
        with self.assertRaises(TelefonoInvalidoError):
            Dueno(nombre="Carlos", telefono="123", direccion="Calle 1", documento="123")

    def test_nombre_vacio(self):
        """
        Prueba que la creación de un Dueno con un nombre vacío o solo espacios
        lance la excepción DatoInvalidoError.
        """
        with self.assertRaises(DatoInvalidoError):
            Dueno(nombre="   ", telefono="3101234567", direccion="Calle 1", documento="123")

if __name__ == '__main__':
    unittest.main()