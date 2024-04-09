
# Crear una clase Articulo:

#   - nombre: str

#   - precio: float

#   - __str__()

class Articulo:
    """Son productos con un nokmbre y un precio"""
    def __init__(self, nombre:str, precio:float) -> None:
        self.nombre=nombre
        self.precio=precio
    def __str__(self):
        return f'Artículo: {self.nombre} al precio de: ${self.precio: .2f}'

#articulo = Articulo("Pera",150.222)
#print(articulo)