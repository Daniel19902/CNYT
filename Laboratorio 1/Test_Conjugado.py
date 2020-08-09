import unittest
import Conjugado


class TestModulo(unittest.TestCase):

    def test_conjugado(self):
        self.assertEqual(Conjugado.conjugado("8 - 9i"), "8 + 9i")

    def test_conjugado1(self):
        self.assertEqual(Conjugado.conjugadoSuma("2 + 2i", "2 + 4i"), "4 - 6i")

    def test_conjugado2(self):
        self.assertEqual(Conjugado.conjugadoMultiplicacion("-100, -1", "-9 , -8"), "892 - 809i")


if __name__ == "__main__":
    unittest.main()
