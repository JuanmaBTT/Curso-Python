"""
5) Escribe un programa que pida al usuario un número entero del 0 al 9, y que mientras el número no sea correcto se repita el proceso. Luego debe comprobar si el número se encuentra en la lista de números y notificarlo:
🖐 Ayuda: La sintaxis "valor in lista" permite comprobar fácilmente si un valor se encuentra en una lista (devuelve True o False).

"""
###5) Escribe un programa que pida al usuario un número entero del 0 al 9, y que mientras el número no sea
### correcto se repita el proceso. Luego debe comprobar si el número se encuentra en la lista de números y 
### notificarlo:

###🖐 Ayuda: La sintaxis "valor in lista" permite comprobar fácilmente si un valor se encuentra en una lista
### (devuelve True o False).


"""def seleccion_numero():
    while   True:
        numero = int(input('¿Podrías indicarme un número entero del 1 al 10?'))
        if numero>mayor_0 and numero<menor_10:
            return print(f'Correcto, el número {numero} cumple con los requisitos y no esta en la lista!')
        else: input('No es correcto.')
def añadir_a_lista(numero:int):
    lista_de_numeros.append(numero)
    print(lista_de_numeros)

def main():
    numero = seleccion_numero()
    lista_resultante = añadir_a_lista(numero)
main()"""

numero = input('¿Podrías indicarme un número entero del 1 al 10?')
lista_de_numeros=["1","2","3"]
mayor_0=0
menor_10=10

while not numero.isdigit():
            numero =input("Error, ¿Podrías indicarme un número?")
while numero.isdigit() :
        if int(numero)<mayor_0 or int(numero)>menor_10:
            print(f'El número {numero} no cumple con los requisitos.')
            numero =input("¿Podrías indicarme un número que cumpla los requisitos?")               
        elif    numero in lista_de_numeros:
            print(f'El número {numero} ya está en el listado.')
            numero =input("¿Podrías indicarme un número que cumpla los requisitos?")
        else :
            print(f'Correcto, el número {numero} cumple con los requisitos y no esta en la lista!')
            break
lista_de_numeros.append(numero)
print(lista_de_numeros)
