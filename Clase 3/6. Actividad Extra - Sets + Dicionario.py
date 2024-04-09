"""Consigna Sets

Crear un conjunto en Python que posea los siguientes elementos:
Países: Inglaterra, USA, México.
Posteriormente agrega nuestro set de países, los elementos de: Islandia, Italia, Argentina y Portugal, USA
Elimina a los países: Chile e Italia
Pregunta: ¿Qué pasa si queremos eliminar al país Chile utilizando el método remove?, ¿Qué pasó con el element de USA?"""

paises = {"Inglaterra", "USA", "México"}
print(paises)
paises.update(["Islandia", "Italia", "Argentina", "Portugal","USA"])
print(paises)
paises.discard("Chile")
paises.discard("Italia")
print(paises)
#En update, cuando volvimos a poner a USA no se duplicó, por otro lado, si queremos eliminar a Italia con Remove da error.