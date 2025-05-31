import unittest
from unittest.mock import patch
from services.gestion import crear_consulta
from models.consulta import Consulta
from models.mascota import Mascota
from models.dueno import Dueno

class TestCrearConsulta(unittest.TestCase):
    """
    Clase de pruebas unitarias para la función crear_consulta.

    Pruebas:
        - test_crear_consulta_exitosa: Verifica que se cree una consulta correctamente 
          para una mascota registrada y que se muestre el mensaje de confirmación.
        - test_crear_consulta_mascota_no_registrada: Verifica que se maneje correctamente 
          el caso cuando la mascota no está registrada, sin crear una consulta.
    """

    def setUp(self):
        """
        Configura el entorno de pruebas inicializando una mascota con su dueño
        y listas vacías para las consultas.
        """
        dueno = Dueno("Juan Pérez", "1234567890", "Calle Falsa 123", "12345")
        mascota = Mascota("Firulais", "Perro", "Labrador", "3", dueno)
        self.mascotas = {"Firulais": mascota}
        self.consultas = []

    def test_crear_consulta_exitosa(self):
        """
        Prueba que la función crear_consulta registre correctamente una consulta
        cuando la mascota existe y los datos son válidos.
        También verifica que se imprima el mensaje de éxito esperado.
        """
        inputs = ["Firulais", "01/06/2025", "Vacunación", "Sin síntomas"]
        with patch('builtins.input', side_effect=inputs), patch('builtins.print') as mock_print:
            crear_consulta(self.mascotas, self.consultas)

        self.assertEqual(len(self.consultas), 1)
        self.assertEqual(self.consultas[0].motivo, "Vacunación")
        mock_print.assert_any_call("Consulta registrada correctamente para Firulais ✓")

    def test_crear_consulta_mascota_no_registrada(self):
        """
        Prueba que la función crear_consulta no registre una consulta cuando
        la mascota no está registrada y se muestre el mensaje de error esperado.
        """
        inputs = ["NoExiste"]
        with patch('builtins.input', side_effect=inputs), patch('builtins.print') as mock_print:
            crear_consulta(self.mascotas, self.consultas)

        self.assertEqual(len(self.consultas), 0)
        mock_print.assert_any_call("\nNo se encontró una mascota registrada con el nombre NoExiste.")

if __name__ == '__main__':
    unittest.main()