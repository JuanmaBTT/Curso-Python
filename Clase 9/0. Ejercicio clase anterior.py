"""
Crear una función llamada es_multiplo que tome dos números como argumentos 
y determine si alguno de ellos es múltiplo del otro. 
La función debe devolver True si alguno de los números es múltiplo del otro, 
y False en caso contrario.
Luego, en el programa principal, 
llamar a la función es_multiplo con dos números de prueba 
y mostrar el resultado en pantalla.
"""
def ingreso_numeros() ->tuple[int,int]:
    numero_1=int(input("Número 1:"))
    numero_2=int(input("Número 2:"))
    return numero_1, numero_2

def es_multiplo(numero_1:int,numero_2:int) ->bool:
    if numero_1 % numero_2 ==0 or numero_2%numero_1==0:
        return True
    else :
        return False
def mostrar_resultado(resultado: bool,numero_1: int,numero_2: int):
    if resultado == True:
        print(f'El número {numero_1} es múltiplo de {numero_2} o el número {numero_2} es múltplo de {numero_1}')
    else :
        print(f'Ni el número {numero_1} es múltiplo de {numero_2}, ni el número {numero_2} es múltiplo del número {numero_1}')

def main():
    numero_1, numero_2 = ingreso_numeros()
    resultado = es_multiplo(numero_1,numero_2)
    mostrar_resultado(resultado,numero_1,numero_2)

main()
