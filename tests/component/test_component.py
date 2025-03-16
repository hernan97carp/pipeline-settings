import unittest
from src.main import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()     
    def test_add(self):
        self.assertEqual(self.calc.add(1,2),3)
        
if __name__ == '__main__':
    unittest.main()
    
#La función principal es comprobar que el método add de la clase Calculator funcione.