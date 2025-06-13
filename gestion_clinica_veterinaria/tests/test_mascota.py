import unittest
from unittest.mock import patch
from models.dueno import Dueno
from models.mascota import Mascota
from exceptions.errores import DatoInvalidoError, EdadInvalidaError

class TestMascota(unittest.TestCase):
    """
    Pruebas unitarias para la clase Mascota y su relación con la clase Dueno.
    Se verifica la validación de datos, la correcta asignación de atributos
    y el manejo de errores personalizados.
    """

    def setUp(self):
        """Crea un dueño y una mascota válida para usar en las pruebas."""
        self.dueno = Dueno("Carlos", "1234567890", "Calle 1", "123467890")
        self.mascota = Mascota("Firulais", "Perro", "Labrador", "5", self.dueno)

    def test_atributos_mascota(self):
        """Verifica que los atributos de la mascota se asignen correctamente."""
        self.assertEqual(self.mascota.nombre, "Firulais")
        self.assertEqual(self.mascota.especie, "Perro")
        self.assertEqual(self.mascota.raza, "Labrador")
        self.assertEqual(self.mascota.edad, 5)

    def test_mascota_tiene_dueno(self):
        #Verifica que la mascota tenga un dueño asociado correctamente.
        self.assertIsInstance(self.mascota.dueno, Dueno)
        self.assertEqual(self.mascota.dueno.nombre, "Carlos")
        self.assertEqual(self.mascota.dueno.documento, "123467890")

    def test_dueno_compartido(self):
        #Verifica que dos mascotas puedan compartir el mismo dueño.
        otra_mascota = Mascota("Max", "Perro", "Golden", "3", self.dueno)
        self.assertEqual(otra_mascota.dueno, self.mascota.dueno)
        self.assertEqual(otra_mascota.dueno.nombre, "Carlos")

    def test_nombre_vacio(self):
        #Valida que se lance una excepción si el nombre de la mascota está vacío.
        with self.assertRaises(DatoInvalidoError) as context:
            Mascota("", "Perro", "Labrador", 5, self.dueno)
        self.assertIn("nombre", str(context.exception))

    def test_edad_decimal(self):
        #Valida que no se acepten edades decimales para la mascota.
        with self.assertRaises(EdadInvalidaError) as context:
            Mascota("Firulais", "Perro", "Labrador", 4.5, self.dueno)
        self.assertIn("edad", str(context.exception))

    def test_edad_negativa(self):
        #Valida que no se acepten edades negativas para la mascota.
        with self.assertRaises(EdadInvalidaError) as context:
            Mascota("Firulais", "Perro", "Labrador", -1, self.dueno)
        self.assertIn("edad", str(context.exception))

    def test_edad_no_entero(self):
        #Valida que se lance error si la edad no es un número válido.
        with self.assertRaises(EdadInvalidaError) as context:
            Mascota("Firulais", "Perro", "Labrador", "cinco", self.dueno)
        self.assertIn("edad", str(context.exception))

    def test_dueno_invalido(self):
        #Verifica que se lance excepción si el dueño no es una instancia válida.
        with self.assertRaises(DatoInvalidoError) as context:
            Mascota("Firulais", "Perro", "Labrador", 5, "no es un dueno")
        self.assertIn("dueño", str(context.exception))

    def test_todos_los_campos_validos(self):
        #Verifica que no se lance ninguna excepción si los datos son correctos.
        try:
            mascota = Mascota("Firulais", "Perro", "Labrador", 5, self.dueno)
        except Exception:
            self.fail("Mascota con datos válidos lanzó una excepción inesperada")

if __name__ == "__main__":
    unittest.main()


