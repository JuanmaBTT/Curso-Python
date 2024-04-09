from Modelos.personas import Usuario #El primer script utiliza IMPORTACIÓN ABSOLUTA.
from Modelos.articulo import Articulo
from Modelos.pedidos import Pedido
from pprint import pprint

juan = Usuario("Juan","juan@gmail.com","123")
pau = Usuario("Pau","pau@gmail.com","987")

# print(juan)
# print(pau)

pera = Articulo("Pera",150.222)
manzana = Articulo("Manzana",50)

# print(pera)
# print(manzana)

pedido1 = Pedido(juan,pera)
pedido2 = Pedido(pau,pera)
pedido3 = Pedido(pau,manzana)
pedido4 = Pedido(juan,manzana)

# print(pedido1)
# print(pedido2)
# print(pedido3)
# print(pedido4)
pprint(Pedido.lista_de_pedidos)