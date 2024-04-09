"""
4) Escribe un programa que pida al usuario cuantos números quiere introducir. Luego lee todos los números y realiza una media aritmética.

"""
### 4) Escribe un programa que pida al usuario cuantos números quiere introducir. 
### Luego lee todos los números y realiza una media aritmética.

def cantidad_de_numeros() -> int:
    cantidad = int(input("¿Cuántos números desea introducir?: "))
    return cantidad

def seleccion_numeros(cantidad:int):
    for i in range(0,cantidad):
        numeros = int(input("¿Indique un número: "))
    return numeros

def media(*numeros) -> float:
        promedio=sum(numeros)/len(numeros)
        return promedio 
def respuesta(resultado) :
      print(f'El promedio es:{resultado}' )

def main():
        cantidad= cantidad_de_numeros()
        numeros= seleccion_numeros(cantidad)
        resultado=media(numeros)
        respuesta(resultado)
main()
