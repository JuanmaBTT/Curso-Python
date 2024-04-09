conjunto_productos = {"leche", "pan", "huevos", "arroz", "frijoles"}
otro_conjunto_productos = {"pan", "papas", "zanahorias", "huevos", "tomates"}

respuesta = "leche" in conjunto_productos
print(respuesta)
respuesta = "leche" in otro_conjunto_productos
print(respuesta)

# conjunto_productos.update(otro_conjunto_productos)
# print(conjunto_productos)

print(conjunto_productos.difference(otro_conjunto_productos))
print(conjunto_productos - otro_conjunto_productos)

print(conjunto_productos.intersection(otro_conjunto_productos))
print(conjunto_productos & otro_conjunto_productos)

from pprint import pprint

print(conjunto_productos.symmetric_difference(otro_conjunto_productos))