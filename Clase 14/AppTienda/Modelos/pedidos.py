
# Crear clase Pedido:

#   - variable de clase: lista_de_pedidos = []

#   - variables de instancia:

#       - usuario: Usuario

#       - articulo: Articulo

#   - __str__()

from .personas import Usuario #El resto de scripts utilizan IMPORTACIONES RELATIVAS. Es decir, se debe aplicar con un punto (.) previo a importar el módulo.
from .articulo import Articulo

class Pedido():
    """Consiste en un usuario que compra un artículos y se guarda en una lista de pedidos"""
    lista_de_pedidos: list["Pedido"] = []

    def __init__(self, usuario:Usuario, articulo:Articulo) -> None:
        self.usuario = usuario
        self.articulo = articulo
        Pedido.lista_de_pedidos.append(self)
    def __str__(self):
        return f'{self.usuario} compró el {self.articulo}'
    def __repr__(self):
        return f'{self.usuario} compró el {self.articulo}'
# cliente = Usuario("Juan","juan@gmail.com","123")
# articulo = Articulo("Pera",150.222)
# pedido1 = Pedido(cliente,articulo)
# print(pedido1)
# print(Pedido.lista_de_pedidos)