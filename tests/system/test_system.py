
import unittest
from src.main import System

class TestSystem(unittest.TestCase):
    def setUp(self):
        self.system = System()

    def test_perform_add(self):
        self.assertEqual(self.system.perform_operation('add', 1, 2), 3)

if __name__ == '__main__':
    unittest.main()