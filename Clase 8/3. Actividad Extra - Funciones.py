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
###Mi respuesta (estaba OK):

def seleccion_año() -> int:
    año = int(input("¿Me podrías decir un año?"))
    return año
def año_bisiesto(año:int) -> bool:
    if (año % 4==0 or año %400==0) and año %100!=0 :
        return True
    elif año %400==0:
        return True
    else :
        return False
def mostrar_resultado(respuesta: bool,año: int) -> None:
    """Muestra el resultado de la función año_bisiesto()"""
    if respuesta == True:
        print(f"El año {año} es bisiesto")
    else:
        print(f"El año {año} no es bisiesto")
def main():
    año = seleccion_año()
    respuesta = año_bisiesto(año)
    mostrar_resultado(respuesta, año)

main()