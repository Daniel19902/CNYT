import unittest
import Fase


class TestSuma(unittest.TestCase):

    def test_fase(self):
        self.assertEqual(Fase.fase(9, 10), 0.84)

    def test_fase1(self):
        self.assertEqual(Fase.fase(-9, 10), -0.84)

    def test_fase2(self):
        self.assertEqual(Fase.fase(-51, 100), -1.1)


if __name__ == "__main__":
    unittest.main()
