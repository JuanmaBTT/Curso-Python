"""
from dataclasses import dataclass

@dataclass
class Persona:
    dni: int
    nombres: str
    apellidos: str
    nacimiento: str
"""

class Persona:

    ser_vivo = True   # variables de clase

    def __init__(self, dni: int, nombres: str, apellidos: str, nacimiento: str):  # método o constructor
        print("Se creó un objeto...")
        self.dni = dni  # atributo / variable de instancia
        self.nombres = nombres  # atributo / variable de instancia
        self.apellidos = apellidos  # atributo / variable de instancia
        self.nacimiento = nacimiento  # atributo / variable de instancia


juan = Persona(123, "Juan", "brusco", "1/1/2000")
# ☝🏻 objeto. Instancia de la clase Persona
luis = Persona(dni=888, nombres="Luis", apellidos="López", nacimiento="2/2/1990")
# ☝🏻 objeto. Instancia de la clase Persona

# print()
# print(juan.ser_vivo)
# print(luis.ser_vivo)
# Persona.ser_vivo = False
# print(juan.ser_vivo)
# print(luis.ser_vivo)
lista_personas = [juan, luis]
for persona in lista_personas:
    print(persona.dni, persona.nombres, persona.apellidos)