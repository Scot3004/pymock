import unittest
from mi_paquete.mi_modulo import Original

class OriginalTestCase(unittest.TestCase):
    def test_saludo(self):
        original = Original()
        self.assertEqual('saludos Sergio, soy original',
        original.saludo('Sergio'))