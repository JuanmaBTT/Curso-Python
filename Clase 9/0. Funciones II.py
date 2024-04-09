def introducir_numeros() -> tuple[int, int]:
    """Introduce 2 números"""
    numero_1 = int(input("Número 1: "))
    numero_2 = int(input("Número 2: "))
    return numero_1, numero_2


def es_multiplo(numero1: int, numero2: int) -> bool:
    """Determina si un número es múltiplo de otro"""
    if numero1 % numero2 == 0:
        return True
    elif numero2 % numero1 == 0:
        return True
    else:
        return False
def mostrar_resultado(respuesta: bool) -> None:
    """Muestra el resultado de la función es_multiplo()"""
    if respuesta == True:
        print("Son múltiplos")
    else:
        print("No son múltiplos")


def main():
    numero_1, numero_2 = introducir_numeros()
    respuesta = es_multiplo(numero_1, numero_2)
    mostrar_resultado(respuesta)


main()

def division(numero1, numero2):
    """Argumentos por posición"""
    return numero1 / numero2


resultado = division(8, 2)
print(resultado)


def division2(numero1, numero2):
    """Argumentos por nombre"""
    return numero1 / numero2


resultado1 = division2(numero2=2, numero1=8)
print(resultado1)

# Funciones con parámetros por defecto (opcionales)
def division1(numero1, numero2=2):
    return numero1 / numero2

print(division1(300))
print(division1(300, 3))