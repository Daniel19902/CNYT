import unittest
import Modulo


class TestModulo(unittest.TestCase):

    def test_modulo(self):
        self.assertEqual(Modulo.modulo("-7 - 9i"), 11.40)

    def test_modulo1(self):
        self.assertEqual(Modulo.modulo("10 - 20i"), 22.36)

    def test_modulo2(self):
        self.assertEqual(Modulo.modulo("70 + 100i"), 122.07)

    def test_modulo3(self):
        self.assertEqual(Modulo.modulo("-30 + 1i"), 30.02)


if __name__ == "__main__":
    unittest.main()
