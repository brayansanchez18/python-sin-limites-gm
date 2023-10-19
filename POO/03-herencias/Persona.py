# clase padre PERSONA
class Persona:
    def __init__(self, nombre, edad) -> None:
        self.nombre = nombre
        self.edad = edad
    
    def __str__(self) -> str:
        return f'persona: {self.nombre} {self.edad}'

# case hija EMPLEADO
class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo) -> None:
        super().__init__(nombre, edad) # <- con el metodo super accedemos a los atributos de la clse padre
        self.sueldo = sueldo

    def __str__(self) -> str:
        return f'{super().__str__()} {self.sueldo}'