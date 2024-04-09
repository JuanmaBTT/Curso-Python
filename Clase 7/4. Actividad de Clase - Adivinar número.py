"""
Escribe un programa que genere un número aleatorio entre 1 y 20,
y le pida al usuario que adivine el número. Si el usuario adivina el número,
el programa debe imprimir "¡Adivinaste el número!"
y terminar. Si el usuario no adivina el número,
el programa debe imprimir "El número es mayor"
o "El número es menor", dependiendo de si el número generado
 es mayor o menor que el número ingresado por el usuario.
El programa debe permitir al usuario intentar adivinar
el número 5 veces.
"""

import random
num_aleatorio = random.randint(1, 20)
intentos=0

while intentos<5:
    adivinar_número=int(input("Adivina el número: "))
    if adivinar_número == num_aleatorio :
        print("¡Adivinaste el número!")
    elif adivinar_número < num_aleatorio :
        print("El número es mayor")
    elif adivinar_número > num_aleatorio :
        print("El número es menor")
    intentos+=1