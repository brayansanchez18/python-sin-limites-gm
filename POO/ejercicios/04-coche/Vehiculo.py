class Vehiculo:
    def __init__(self, color, ruedas) -> None:
        self.color = color
        self.ruedas = ruedas

    def __str__(self) -> str:
        return f'vehiculo [color: {self.color}, ruedas: {self.ruedas}]'
    
class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad) -> None:
        super().__init__(color, ruedas)
        self.velocidad = velocidad
        
    def __str__(self) -> str:
        return f'{super().__str__()} velocidad: {self.velocidad}km/hr'

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo) -> None:
        super().__init__(color, ruedas)
        self.tipo = tipo
        
    def __str__(self) -> str:
        return f'{super().__str__()} tipo: {self.tipo}'