import unittest
import Carteciano



class TestSuma(unittest.TestCase):

    def test_carteciano(self):
        self.assertEqual(Carteciano.carteacianoAPolar(9, 90), "p = 90 , angulo = 1")

    def test_carteciano1(self):
        self.assertEqual(Carteciano.polarACarteciano(9, 90), "-4 + 8i")
    
if __name__ =="__main__":
    unittest.main()