"""
Realiza una función que, dependiendo de los parámetros que reciba,
convierta a milímetros o a metros.
1- Si recibe un argumento, supone que son milímetros y convierte a metros,
centímetros y milímetros.
2- Si recibe 3 argumentos, supone que son metros, centímetros y milímetros
y los convierte a milímetros.
"""

def convertir_longitud(*args):
    if len(args) == 1:
        milimetros = args[0]
        metros = milimetros / 1000
        centimetros = milimetros / 10
        return metros, centimetros, milimetros
    elif len(args) == 3:
        metros, centimetros, milimetros = args
        return (metros * 1000) + (centimetros * 10) + milimetros
    else:
        return False

def main():
    # conversion = convertir_longitud(13, 100, 5)
    # conversion = convertir_longitud(23005)
    # conversion = convertir_longitud(23005, 100, 323, 323)
    medidas = [(123_000, 1212, 99), (1234,), (234, 4343)]
    for tupla in medidas:
        conversion = convertir_longitud(*tupla)
        if conversion:
            print(conversion)
        else:
            print("Error de argumentos")

main()