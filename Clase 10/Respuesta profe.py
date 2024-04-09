"""
Realizar una función llamada año_bisiesto:
Recibirá un año por parámetro
Imprimirá “El año año es bisiesto” si el año es bisiesto
Imprimirá “El año año no es bisiesto” si el año no es bisiesto
Si se ingresa algo que no sea número, debe indicar que se ingrese un número.
Información a tener en cuenta:
Se recuerda que los años bisiestos son múltiplos de 4, pero los múltiplos de 100 no lo son, 
aunque los múltiplos de 400 sí. Estos son algunos ejemplos de posibles respuestas: 
2012 es bisiesto, 2010 no es bisiesto, 2000 es bisiesto, 1900 no es bisiesto.
"""
def introducir_año() -> int:
    """Ingresa un año determinado"""
    año = int(input("Introducir el año: "))
    return año

def es_bisiesto(año: int) -> bool:
    """Determina si un año es bisiesto"""
    es_multiplo_de_4 = (año % 4 == 0)
    no_es_multiplo_de_100 = not (año % 100 == 0)
    es_mulitplo_de_400 = (año % 400 == 0)

    if es_multiplo_de_4 and (no_es_multiplo_de_100 or es_mulitplo_de_400):
        return True
    else:
        return False
def mostrar_resultado(año: int, resultado: bool):
    """Muestra el resultado de la función es_bisiesto()"""
    if resultado == True:
        print(f"El año {año} es bisiesto")
    else:
        print(f"El año {año} no es bisiesto")

def main():
    año = introducir_año()
    resultado = es_bisiesto(año)
    mostrar_resultado(año, resultado)

main()