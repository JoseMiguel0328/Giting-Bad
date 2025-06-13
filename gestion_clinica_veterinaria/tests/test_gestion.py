import unittest
from unittest.mock import patch, mock_open
from services import gestion

class TestGestion(unittest.TestCase):
    """
    Pruebas unitarias para funciones del módulo gestion.
    Se cubren funciones relacionadas con el manejo de mascotas y archivos.
    """

    def setUp(self):
        """Inicializa diccionarios vacíos para cada prueba."""
        self.mascotas = {}
        self.duenos = {}
        self.consultas = []

    def test_listar_mascotas_vacia(self):
        """Verifica que se imprima mensaje cuando no hay mascotas registradas."""
        with patch('builtins.print') as mocked_print:
            gestion.listar_mascotas(self.mascotas)
            mocked_print.assert_any_call("No hay mascotas registradas.")

    def test_crear_mascota_con_nuevo_dueno(self):
        """
        Simula la creación de una nueva mascota y un nuevo dueño mediante inputs
        y verifica que se guarden correctamente en los diccionarios.
        """
        inputs = ["Firulais", "Perro", "Labrador", "5", "123467890", "Carlos", "1234567890", "Calle 1"]
        with patch('builtins.input', side_effect=inputs), \
            patch('builtins.print'), \
            patch("builtins.open", mock_open()) as mocked_file:
            gestion.crear_mascota(self.mascotas, self.duenos)

        self.assertIn("Firulais", self.mascotas)
        self.assertIn("123467890", self.duenos)

if __name__ == '__main__':
    unittest.main()



