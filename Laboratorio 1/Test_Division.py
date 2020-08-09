import unittest
import Division


class TestDivision(unittest.TestCase):

    def test_div(self):
        self.assertEqual(Division.divicion("2 , 2", "2 , 4"), "0.6 - 0.2i")

    def test_div1(self):
        self.assertEqual(Division.divicion("15 , -28", "24 ,-44"), "0.63 - 0.005i")

    def test_div2(self):
        self.assertEqual(Division.divicion("78 ,26", "27 ,-98"), "-0.04 + 0.808i")

    def test_div3(self):
        self.assertEqual(Division.divicion("-100, -1", "-9 , -8"), "6.26 - 5.455i")

    def test_div4(self):
        self.assertEqual(Division.divicion("-1 , 1", "-1 , 1"), "1.0 + 0.0i")


if __name__ == "__main__":
    unittest.main()
