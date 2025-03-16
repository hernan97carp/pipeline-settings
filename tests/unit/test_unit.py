import unittest
from src.main import add

class TestAddFunction(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(1,2),3)
        
if __name__ == '__main__':
    unittest.main()