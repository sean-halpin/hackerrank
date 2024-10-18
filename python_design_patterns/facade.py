# Facade Pattern concise Example

class Subsystem1:
    def operation1(self):
        print('Subsystem1: Ready!')

    def operation2(self):
        print('Subsystem1: Go!')
        
class Subsystem2:
    def operation1(self):
        print('Subsystem2: Ready!')

    def operation2(self):
        print('Subsystem2: Go!')

class Facade:
    def __init__(self):
        self._subsystem1 = Subsystem1()
        self._subsystem2 = Subsystem2()

    def operation(self):
        self._subsystem1.operation1()
        self._subsystem1.operation2()
        self._subsystem2.operation1()
        self._subsystem2.operation2()