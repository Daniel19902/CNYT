import unittest
import Suma


class TestSuma(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(Suma.sumaComplejo("2 + 2i", "2 + 4i"), "4 + 6i")

    def test_sum1(self):
        self.assertEqual(Suma.sumaComplejo("15 - 28i", "24 - 44i"), "39 - 72i")

    def test_sum2(self):
        self.assertEqual(Suma.sumaComplejo("78 + 26i", "27 - 98i"), "105 - 72i")

    def test_sum3(self):
        self.assertEqual(Suma.sumaComplejo("-100 - 1i", "-9 - 8i"), "-109 - 9i")

    def test_sum4(self):
        self.assertEqual(Suma.sumaComplejo("-0 + 0i", "-0 + 0i"), "0 + 0i")


if __name__ == "__main__":
    unittest.main()
