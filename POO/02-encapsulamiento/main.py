class Persona:
    def __init__(self, nombre, apellido, edad) -> None:
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad
    
    # get = obtener el valor del atributo
    @property # con el atributo property estamos encapsulando el atributo de nombre
    # y estamos indicando que solo el metodo nombre() puede acceder a este atributo
    def nombre(self):
        return self._nombre

    # set = modificar el valor del atributo
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido
    
    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido
    
    @property
    def edad(self):
        return self._edad
    
    @edad.setter
    def edad(self, edad):
        self._edad = edad
        
    def mostrarDetalle(self):
        print(f'persona: {self._nombre} {self._apellido} {self._edad}')

    def __del__(self):
        print(f'persona: {self._nombre} {self._apellido}')