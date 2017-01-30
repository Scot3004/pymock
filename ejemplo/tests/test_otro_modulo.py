import unittest
from mock import patch, Mock, sentinel
from mi_paquete.otro_modulo import saludo_foraneo, soy_vago

class SaludoOriginalTestCase(unittest.TestCase):
    def test_saludo(self):
        self.assertEqual('saludos Pythonist, soy original',
        saludo_foraneo())

    @patch('mi_paquete.otro_modulo.Original.saludo')
    def test_mock_saludo(self, mock_saludo):
        mock_saludo.return_value = 'cambie la salida'
        self.assertEqual('cambie la salida',
        saludo_foraneo())

    @patch('mi_paquete.otro_modulo.Original.saludo')
    def test_mock_sentinel_saludo(self, mock_saludo):
        mock_saludo.return_value = sentinel.salida
        self.assertEqual(sentinel.salida,
        saludo_foraneo())

    @patch('mi_paquete.otro_modulo.Original.saludo')
    def test_mock_raise_saludo(self, mock_saludo):
        mock_saludo.side_effect = ValueError('Lo hice reventar')
        self.assertRaises(ValueError)

    @patch('mi_paquete.otro_modulo.Original.saludo')
    def test_mock_multiple_saludo(self, mock_saludo):
        mock_saludo.side_effect = [sentinel.salida1, sentinel.salida2]
        self.assertEqual(sentinel.salida1,
        saludo_foraneo())
        self.assertEqual(sentinel.salida2,
        saludo_foraneo())

    @patch('mi_paquete.otro_modulo.Original.saludo')
    def test_mock_call_saludo(self, mock_saludo):
        saludo_foraneo()
        mock_saludo.assert_called_with('Pythonist')

