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
    def __init__(self, pais) -> None:
        self.pais = pais

class Cliente(Pais):
    def __init__(self, pais_de_origen, nombre, apellido, nacimiento) -> None:
        super().__init__(pais_de_origen)
        self.nombre = nombre
        self.apellido = apellido
        self.nacimiento = nacimiento

cliente1 = Cliente("Uruguay", "Juan", "Lincon", "2000")

print(cliente1.__dict__)