import unittest
from unittest.mock import patch
from src.main import System

class TestSystemIntegration(unittest.TestCase):
    @patch('src.main.Calculator.add')
    def test_integration_with_external_service(self, mock_add):
        mock_add.return_value = 3
        system = System()
        result = system.perform_operation('add', 1, 2)
        self.assertEqual(result, 3)

if __name__ == '__main__':
    unittest.main()
#El propósito es Usar un mock para simular un servicio externo y verifica la integración.
