""" 
Descripción de la actividad. 

Calcular la suma de una cantidad de números enteros ingresados por el usuario directamente utilizando la función input (). 

Para finalizar la ejecución del programa, el usuario debe escribir la palabra exit(). El programa debe validar dicha acción. 

Finalmente, el algoritmo debe mostrar la suma parcial y total obtenida.
"""

numero =input("¿Podrías indicarme un número?")
suma = 0



while not numero.isdigit() and numero !="exit" :
            numero =input("Error, ¿Podrías indicarme un número?")

while numero.isdigit():
        suma += int(numero)
        print(f'La suma es {suma}')
        print(f'El número añadido es {numero}') 
        numero = input("¿Podrías indicarme otro número?")
        if not numero.isdigit() and numero !="exit" :
            numero =input("Error, ¿Podrías indicarme un número?")
        elif numero =="exit":
            print(f'El programa ha terminado.')
while not numero.isdigit() and numero !="exit" :
            numero =input("Error, ¿Podrías indicarme un número?")

while numero.isdigit():
        suma += int(numero)
        print(f'La suma es {suma}')
        print(f'El número añadido es {numero}') 
        numero = input("¿Podrías indicarme otro número?")
        if not numero.isdigit() and numero !="exit" :
            numero =input("Error, ¿Podrías indicarme un número?")
        elif numero =="exit":
            print(f'El programa ha terminado.')

if numero =="exit":
            print(f'El programa ha terminado.')


"""
while not numero.isdigit() and numero !="exit" :
            numero =input("Error, ¿Podrías indicarme un número?")
if numero.isdigit():
        suma += int(numero)
        print(f'La suma es {suma}')
        print(f'El número añadido es {numero}') 
        numero = input("¿Podrías indicarme otro número?")
        if not numero.isdigit() and numero !="exit" :
            numero =input("Error, ¿Podrías indicarme un número?")
        elif numero =="exit":
            print(f'El programa ha terminado.')
"""

""" Primera prueba Jm:

numero_1 =input("¿Podrías indicarme un número?")

numero_2 =input("¿Podrías indicarme otro número?")

suma = int(numero_1) + int(numero_2)

while numero_1 or numero_2 != "exit":
    resultado = print(f'La suma de {numero_1} y {numero_2} es {suma}')
    if numero_1 == "exit" or numero_2 == "exit":
        break
else : print(f'El programa ha finalizado')

numero_1 =input("¿Podrías indicarme un número?")

numero_2 =input("¿Podrías indicarme otro número?")

"""


###Solución profe

"""
while continuar:
    entrada = input("Ingresa un número ('exit' para terminar): ")
    if entrada == "exit":
        continuar = False
    else:
        if entrada.isdigit():
            numero = int(entrada)
            # suma = suma + numero
            suma += numero
            print(f"La suma parcial es {suma}")
        else:
            print("*** Debes introducir un número ***")

print(f"La suma final es {suma}")

"""