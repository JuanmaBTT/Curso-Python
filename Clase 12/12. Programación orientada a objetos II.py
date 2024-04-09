"""
Crea una clase llamada "Círculo" que represente un círculo. 
La clase debe tener un atributo de clase llamado "pi" 
con un valor constante de 3.14159. 
Además, la clase debe tener un atributo de instancia "radio" 
que se recibe como argumento en el constructor.
La clase "Círculo" debe tener un método llamado 
"calcular_area" que calcule y devuelva el área del círculo 
utilizando la fórmula: area = pi * radio ^ 2.
Escribe el código de la clase "Círculo" 
a) crea una instancia de la misma. 
b) Luego, accede al atributo de clase "pi" 
c) y utiliza el método "calcular_area" para obtener y mostrar el área del círculo.
"""
class Circulo:
    pass

    # variable de clase
    import math
    PI = math.pi
    
    # Constructor
    def __init__(self, radio):
        self.radio = radio
    
    # Método para calcular el área del círculo
    def calcular_area(self):
        area = self.PI * self.radio ** 2
        return area

# Creo una instancia de la clase Círculo
circulo = Circulo(10)

# Accedo al atributo de clase "pi"
valor_pi = circulo.PI
print("Valor de pi:", valor_pi)

# Calculo y muestro el área del círculo
area_circulo = circulo.calcular_area()
print("Área del círculo:", area_circulo)

""" 
Crear una clase producto que tenga como variables de instancia nombre y precio. 
Esta clase tiene un método para modificar el precio con procentaje, 
le quiero pasar un float: se va a llamar modificar_precio. 
Entonces, cuando cree una instancia: producto_a va a ser una instancia de Producto.
"""
class Producto1:
    def __init__(self, nombre: str, precio: float) -> None:
        self.nombre = nombre
        self.precio = precio
    def modificar_precio(self, nuevo_valor: float):
        self.precio *= nuevo_valor

producto1 = Producto1("Camisa", 100)
producto2 = Producto1("Pantalón", 50)
print(f"{producto1.nombre} ${producto1.precio:.2f}")
print(f"{producto2.nombre} ${producto2.precio:.2f}")
producto1.modificar_precio(1.25)
producto2.modificar_precio(0.50)
print()
print(f"{producto1.nombre} ${producto1.precio:.2f}")
print(f"{producto2.nombre} ${producto2.precio:.2f}")

class Persona1:
    def __init__(self, nombres:str, apellidos:str):  
        self.nombres = nombres
        self.apellidos = apellidos  
    def __str__(self) -> str:
        return f"{self.apellidos.capitalize()}, {self.nombres.capitalize()}"

juan = Persona1("Juan", "brusco")
luis = Persona1(nombres="Luis", apellidos="López")
print(juan)
print(luis)

class Persona:
    def __init__(self, dni:int, nombres:str, apellidos:str):
        self.dni = dni
        self.nombres = nombres
        self.apellidos = apellidos  
    def __str__(self) -> str:
        return f"{self.apellidos.capitalize()}, {self.nombres.capitalize()}: DNI {self.dni}"

juan = Persona(123, "Juan", "brusco")
luis = Persona(dni=555, nombres="Luis", apellidos="López")
print(juan)
print(luis)

"""
A partir del código de 3_ejercicio.py (clase Producto),
crear el método especial __str__ que muestre:
     <nombre>: $<precio>
"""
class Producto:
    def __init__(self, nombre: str, precio: float) -> None:
        self.nombre = nombre
        self.precio = precio
    def __str__(self) -> str:
        return f"{self.nombre}: ${self.precio:.2f}"
    
    def modificar_precio(self, nuevo_valor: float):
        self.precio *= nuevo_valor

producto1 = Producto("Camisa", 100)
producto2 = Producto("Pantalón", 50)
print(producto1)
print(producto2)
producto1.modificar_precio(1.25)
producto2.modificar_precio(0.50)
print()
print(producto1)
print(producto2)


