class Persona:
    def __init__(self, nombre, apellido, edad) -> None:
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def mostrarDetalle(self):
        print(f'persona: {self.nombre} {self.apellido} {self.edad}')
        
persona1 = Persona('jazmin', 'santiago', 19)
persona1.mostrarDetalle()

persona2 = Persona('Emanuel', 'sanchez', 22)
persona2.mostrarDetalle()