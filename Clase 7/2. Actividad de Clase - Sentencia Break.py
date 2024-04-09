"""Sentencia break
Descripción de la actividad. 

Observa el código y busca comprender qué sucedió en este caso:
"""

x = 5
while True:
    x -= 1
    print(x)
    if x == 0:
        break
    print("Fin del bucle")

"""Lo sucedido fue que el print no estaba fuera del bucle"""

#Corrección:

x = 5
while True:
    x -= 1
    print(x)
    if x == 0:
        break
    
print("Fin del bucle")
