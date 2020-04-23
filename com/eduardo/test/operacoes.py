from unittest import TestCase
from com.kuma.operacoes import Operacoes

class TestOperacoes(TestCase):
    # Operacoes().soma([1, 3])

    def setUp(self):
        self.operacoes = Operacoes()

    def test_soma(self):
        self.assertEqual(self.operacoes.soma([1, 3]), 5, 'Deveria ser 4')