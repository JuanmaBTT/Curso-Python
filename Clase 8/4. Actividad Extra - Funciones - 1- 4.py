"""
Realiza una función llamada area_rectangulo() que devuelva el área del rectángulo a partir de una base y una altura. Calcula el área de un rectángulo de 15 de base y 10 de altura

🖐 Ayuda: El área de un rectángulo se obtiene al multiplicar la base por la altura.

Realiza una función llamada area_circulo() que devuelva el área de un círculo a partir de un radio. Calcula el área de un círculo de 5 de radio

🖐 Ayuda: El área de un círculo se obtiene al elevar el radio a dos y multiplicando el resultado por el número pi. Puedes utilizar el valor 3.14159 como pi o importarlo del módulo math.
"""
###Realiza una función llamada area_rectangulo() que devuelva el área del rectángulo a partir de una base y una altura. 
###Calcula el área de un rectángulo de 15 de base y 10 de altura
###🖐 Ayuda: El área de un rectángulo se obtiene al multiplicar la base por la altura.


def area_rectangulo(base=15,altura=10):
    area = base*altura
    return print(int(area))

area_rectangulo()

###Realiza una función llamada area_circulo() que devuelva el área de un círculo a partir de un radio. 
###Calcula el área de un círculo de 5 de radio
###🖐 Ayuda: El área de un círculo se obtiene al elevar el radio a dos y multiplicando el resultado por el número pi. 
###Puedes utilizar el valor 3.14159 como pi o importarlo del módulo math.

#Fórmulas
import math
PI= math.pi
def area_circulo(radio=5):
    area = radio**2*PI
    return print(int(area))

area_circulo()

"""
 Realiza una función llamada relacion() que a partir de dos números cumpla lo siguiente:

Si el primer número es mayor que el segundo, debe devolver 1.
Si el primer número es menor que el segundo, debe devolver -1.
Si ambos números son iguales, debe devolver un 0.

Comprueba la relación entre los números: '5 y 10', '10 y 5' y '5 y 5'
"""
num_1=5
num_2=5

def relacion(num_1:int,num_2:int):
    if num_1>num_2:
        return 1
    elif num_1<num_2:
        return -1
    elif num_1==num_2:
        return 0

def resultado (result,num_1,num_2):
    if result==1:
        print(f'El número {num_1} es más grande que el número {num_2}.')
    elif result==-1:
        print(f'El número {num_1} es más chico que el número {num_2}.')
    elif result==0:
        print(f'El número {num_1} es igual que el número {num_2}.')

def main():
    result=relacion(num_1,num_2)
    resultado(result,num_1,num_2)

main()


"""
Realiza una función llamada intermedio() que, a partir de dos números, devuelva su punto intermedio:
🖐 Ayuda: El número intermedio de dos números corresponde a la suma de los dos números dividida entre 2

Comprueba el punto intermedio entre -12 y 24

"""
num_1=-12
num_2=24

def intermedio():
    media=(num_1+num_2)/2
    return print(media)
intermedio()
