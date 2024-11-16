import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
    # Add()
        self.assertEqual(self.calc.add(1,3),4)
        self.assertEqual(self.calc.add(1,4),5)

    #substract()
    def test_substract(self):
        self.assertEqual(self.calc.subtract(2,1),1)
        self.assertEqual(self.calc.subtract(3,1),2)
    
    #multiply()
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2,1),2)
        self.assertEqual(self.calc.multiply(3,2),6)
  
    #dvide()
    def test_divide(self):
        self.assertEqual(self.calc.divide(10,2),5)
        self.assertEqual(self.calc.divide(6,2),3)
    
    #modulo()
    def test_modulo(self):
        self.assertEqual(self.calc.modulo(7,7),0)
        self.assertEqual(self.calc.modulo(10,3),1)

if __name__ == '__main__':
    unittest.main()