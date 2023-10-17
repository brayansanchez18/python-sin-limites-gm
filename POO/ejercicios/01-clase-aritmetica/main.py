class Aritmetica:
    """
    clase aritmetica para realizar las operaciones de suma resta etc
    """
    
    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b
        
    def sumar(self):
        return self.a + self.b
    
    def restar(self):
        return self.a + self.b
    
    def multiplicar(self):
        return self.a * self.b
    
    def dividir(self):
        return self.a / self.b
    
aritmetica1 = Aritmetica(5,3)
print(aritmetica1.sumar())
print(aritmetica1.restar())
print(aritmetica1.multiplicar())
print(aritmetica1.dividir())
