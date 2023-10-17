class cubo:
    def __init__(self, ancho, alto, profundidad) -> None:
        self.ancho = ancho
        self.alto = alto
        self.profundidad = profundidad
    
    def volumen(self):
        return (self.ancho * self.profundidad * self.alto)
    
ancho = int(input('ingresa el ancho: '))
alto = int(input('ingresa el alto: '))
profundo = int(input('ingresa el profundidad: '))

cubo1 = cubo(ancho, alto, profundo)
print(f'el volumen del cubo es: {cubo1.volumen()}')