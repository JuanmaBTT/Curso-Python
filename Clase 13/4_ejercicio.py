"""
Crear 2 clases:
- Pais
    - nombre
- Cliente
    - nombre
    - apellido
    - nacimiento
    - pais_de_origen (FK)
"""

class Pais:
    def __init__(self, nombre:str) -> None:
        self.nombre = nombre

class Cliente:
    def __init__(self, 
                 nombre: str, 
                 apellido: str, 
                 nacimiento: str | None = None, 
                 pais_de_origen: Pais | None = None):
        self.nombre = nombre
        self.apellido = apellido
        self.nacimiento = nacimiento
        self.pais_de_origen = pais_de_origen

# Crear un país
uruguay = Pais("Uruguay")
chile = Pais("Chile")

# Creo un cliente y le asigno el país de origen
cliente1 = Cliente("Juan", "Pérez", "1990-05-15", uruguay)
cliente2 = Cliente("Juana", "Román", "1995-05-25")

# Accedo a los atributosdel cliente
print("Nombre:", cliente1.nombre)
print("Apellido:", cliente1.apellido)
print("Fecha de nacimiento:", cliente1.nacimiento)
print("País de origen:", cliente1.pais_de_origen.nombre)
print()
print("Nombre:", cliente2.nombre)
print("Apellido:", cliente2.apellido)
print("Fecha de nacimiento:", cliente2.nacimiento)
# print("País de origen:", cliente2.pais_de_origen.nombre)