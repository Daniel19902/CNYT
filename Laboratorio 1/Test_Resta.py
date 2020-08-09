import unittest
import Resta


class TestResta(unittest.TestCase):

    def test_res(self):
        self.assertEqual(Resta.resta("2 + 2i", "2 + 4i"), "0 - 2i")

    def test_res1(self):
        self.assertEqual(Resta.resta("15 - 28i", "24 - 44i"), "-9 + 16i")

    def test_res2(self):
        self.assertEqual(Resta.resta("78 + 26i", "27 - 98i"), "51 + 124i")

    def test_res3(self):
        self.assertEqual(Resta.resta("-100 - 1i", "-9 - 8i"), "-91 + 7i")

    def test_res4(self):
        self.assertEqual(Resta.resta("-0 + 0i", "-0 + 0i"), "0 + 0i")


if __name__ == "__main__":
    unittest.main()