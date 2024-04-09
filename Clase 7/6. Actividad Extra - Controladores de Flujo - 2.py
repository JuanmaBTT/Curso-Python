"""
2)  Escribe un programa que lea un número impar por teclado. Si el usuario no introduce un número impar, debe repetirse el proceso hasta que lo introduzca correctamente.
"""
#2)  Escribe un programa que lea un número impar por teclado.
# Si el usuario no introduce un número impar, debe repetirse el proceso hasta que
# lo introduzca correctamente.

def seleccion_numero():
    while   True:
        numero = int(input('¿Podrías indicarme un número impar?'))
        if numero %2==1:
            return print(f'Correcto, el número {numero} es impar!')
        else: input('No es correcto.')

seleccion_numero()

"""
def seleccion_numero():
    numero = int(input('¿Podrías indicarme un número impar?'))
    return numero

def impar(numero:int) -> bool:
    if numero %2==1:
        return True
    else:
        return False
def repeticion_hasta_impar(respuesta:bool,numero:int):
    while respuesta == True:
            return print(f'El número {numero} es impar!')
    else:
            return seleccion_numero()
def main():
    numero = seleccion_numero()
    respuesta = impar(numero)
    repeticion_hasta_impar(respuesta,numero)

main()
"""