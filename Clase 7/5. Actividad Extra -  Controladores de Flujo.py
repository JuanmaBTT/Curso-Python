"""Escribe un programa que lea dos números por teclado y permita elegir entre 4 opciones en un menú:


Mostrar una suma de los dos números
Mostrar una resta de los dos números (el primero menos el segundo)
Mostrar una multiplicación de los dos números
Si elige esta opción se interrumpirá la impresión del menú y el programa finalizará
En caso de no introducir una opción válida, el programa informará de que no es correcta.
"""
def seleccion_numeros() ->tuple[float,float]:
    numero_1 = float(input("¿Podrías indicarme algún número:?"))
    numero_2 = float(input("¿Podrías indicarme otro número:?"))
    return numero_1, numero_2
def menu () :
    print("1- Suma de los números:")
    print('2- Resta de los números:')
    print('3- Multiplicación de los números:')
    print('4- Finalizar programa:')

def seleccion_menu () -> int :
    opcion = int(input("¿Podrías indicarme que operación desearías realizar?"))
    return opcion
def opcion_valida(opcion:int) -> bool:
    if opcion>0 and opcion<5:
       return True
    else :
        return False
def ejecuta_operacion(resultado:bool, opcion:int,numero_1:float,numero_2:float):
    while resultado==True:
        if opcion == 1:
            return print(f'La suma de {numero_1} y {numero_2} es {numero_1+numero_2}')
        elif opcion == 2:
            return print(f'La resta de {numero_1} y {numero_2} es {numero_1-numero_2}')
        elif opcion == 3:
            return print(f'La multiplicación de {numero_1} y {numero_2} es {numero_1*numero_2}')
        elif opcion == 4:
            return exit()
    else :
            return print(f'Opción no es válida, vuelva a intentar:')
  
def main():
    numero_1, numero_2 = seleccion_numeros()
    menu()
    opcion = seleccion_menu()
    resultado = opcion_valida(opcion)
    ejecuta_operacion(resultado,opcion,numero_1,numero_2)

main()