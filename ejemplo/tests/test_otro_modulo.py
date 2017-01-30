import unittest
from mock import patch, Mock
from mi_paquete.otro_modulo import saludo_foraneo

class SaludoOriginalTestCase(unittest.TestCase):
    def test_saludo(self):
        self.assertEqual('saludos Pythonist, soy original',
        saludo_foraneo())

    @patch('mi_paquete.otro_modulo.Original.saludo')
    def test_mock_saludo(self, mock_saludo):
        mock_saludo.return_value = 'cambie la salida'
        self.assertEqual('cambie la salida',
        saludo_foraneo())
