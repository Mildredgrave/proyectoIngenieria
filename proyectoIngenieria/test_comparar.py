import unittest
from juego import comparar

class TestComparar(unittest.TestCase):

    def test_piedra_vs_tijera(self):
        self.assertEqual(comparar("piedra", "tijera"), "gano")

    def test_piedra_vs_papel(self):
        self.assertEqual(comparar("piedra", "papel"), "perdio")

    def test_piedra_vs_piedra(self):
        self.assertEqual(comparar("piedra", "piedra"), "empate")

    def test_papel_vs_piedra(self):
        self.assertEqual(comparar("papel", "piedra"), "gano")

    def test_papel_vs_tijera(self):
        self.assertEqual(comparar("papel", "tijera"), "perdio")

    def test_papel_vs_papel(self):
        self.assertEqual(comparar("papel", "papel"), "empate")

    def test_tijera_vs_papel(self):
        self.assertEqual(comparar("tijera", "papel"), "gano")

    def test_tijera_vs_piedra(self):
        self.assertEqual(comparar("tijera", "piedra"), "perdio")

    def test_tijera_vs_tijera(self):
        self.assertEqual(comparar("tijera", "tijera"), "empate")

if __name__ == '__main__':
    unittest.main()