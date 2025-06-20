from django.test import TestCase
from clinica.models.dueno import Dueno
from clinica_veterinaria.exceptions import DatoInvalidoError, TelefonoInvalidoError, DocumentoInvalidoError

class DuenoValidacionesTest(TestCase):
    def setUp(self):
        self.dueno = Dueno(nombre="Juan Perez", telefono="1234567890", direccion="Calle 1", documento="1234")

    def test_validar_cadena_valida(self):
        self.assertEqual(self.dueno._validar_cadena("maria", "nombre"), "Maria")

    def test_validar_cadena_vacia(self):
        with self.assertRaises(DatoInvalidoError):
            self.dueno._validar_cadena("   ", "nombre")

    def test_validar_telefono_valido(self):
        self.assertEqual(self.dueno._validar_telefono("3216549870"), "3216549870")

    def test_validar_telefono_invalido(self):
        with self.assertRaises(TelefonoInvalidoError):
            self.dueno._validar_telefono("123abc")

    def test_validar_documento_valido(self):
        self.assertEqual(self.dueno._validar_documento(" 5678 "), "5678")

    def test_validar_documento_invalido(self):
        with self.assertRaises(DocumentoInvalidoError):
            self.dueno._validar_documento("abc")