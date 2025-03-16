def add(a,b):
    return a + b
class  Calculator:
    def __init__(self):
        self.result = 0
        
    def add(self, a, b):
        
        self.result = a + b
        return self.result
class System:
    def __init__(self):
        self.calculator = Calculator()
        
    def perform_operation(self, operation, a,b):
        if operation == 'add':
            return self.calculator.add(a,b)
        else:
            raise ValueError('Operacion no soportada')
        
#El Propósito de este archivo es simular un sistema simple con una función, una clase y un sistema completo.
            