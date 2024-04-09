"""ACTIVIDAD EN CLASE
Colecciones 1 Descripción de la actividad.
Utilizando todo lo que sabes sobre cadenas, listas y sus métodos internos, transforma este texto:
gordon lanzó su curva&strawberry ha fallado por un pie! -gritó Joe Castiglione&dos pies -le corrigió Troop&strawberry menea la cabeza como disgustado... -agrega el comentarista

Colecciones 1 Transforma el texto en:
Gordon lanzó su curva...
- Strawberry ha fallado por un pie! -gritó Joe Castiglione.
- Dos pies le corrigió Troop.
- Strawberry menea la cabeza como disgustado... -agrega el comentarista.
Lo único prohibido es modificar directamente el texto"""

cadena="gordon lanzó su curva&strawberry ha fallado por un pie! -gritó Joe Castiglione&dos pies -le corrigió Troop&strawberry menea la cabeza como disgustado... -agrega el comentarista"

""" Lo que había hecho yo:
#print(cadena)
#cadena.replace("&","\n")
#print(cadena.replace("&","...\n").replace("-","\n").title())"""

cadena_separada=cadena.split("&")
print(cadena_separada)
cadena_separada[0]=cadena_separada[0].capitalize() + "..."
cadena_separada[1]=cadena_separada[1].capitalize().replace("joe castiglione","Joe Castiglione") + "."
cadena_separada[2]=cadena_separada[2].capitalize().replace("-le","le").replace("troop","Troop") + "."
cadena_separada[3]=cadena_separada[3].capitalize() + "."
print(cadena_separada)
# print(lista_de_texto)
cadena_nueva = "\n- ".join(cadena_separada)
print(cadena_nueva)
