import unittest
import Multiplicacion


class TestMultiplicacion(unittest.TestCase):

    def test_mult(self):
        self.assertEqual(Multiplicacion.multiply("2 , 2", "2 , 4"), "-4 + 12i")

    def test_mult1(self):
        self.assertEqual(Multiplicacion.multiply("15 , -28", "24 ,-44"), "-872 - 1332i")

    def test_mult2(self):
        self.assertEqual(Multiplicacion.multiply("78 ,26", "27 ,-98"), "4654 - 6942i")

    def test_mult3(self):
        self.assertEqual(Multiplicacion.multiply("-100, -1", "-9 , -8"), "892 + 809i")

    def test_mult4(self):
        self.assertEqual(Multiplicacion.multiply("-0 , 0", "-0 , 0"), "0 + 0i")


if __name__ == "__main__":
    unittest.main()
