class Rectangulo:
    def __init__(self, base, altura) -> None:
        self.base = base
        self.altura = altura
        
    def calcularArea(self):
        return self.base*self.altura
    
base = int(input('proporciona la base: '))
altura = int(input('proporciona la altura: '))
rectangulo1 = Rectangulo(base, altura)
print(f'area del rectangulo: {rectangulo1.calcularArea()}')
