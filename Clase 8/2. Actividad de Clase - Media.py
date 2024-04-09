"""
Escribir una función que reciba una muestra de números en una lista y
 devuelva su media.
"""

def media(lista: list) -> float:
    promedio = sum(lista)/len(lista)
    return promedio
promedio = media([6,8,10])
print(f"La media o el promedio de la muestra de números ingresada en una lista es {promedio}")

"""Escribir una función que reciba una muestra de números 
en una lista y devuelva su media."""

def promediar(notas: list[float]) -> float:
    promedio = sum(notas) / len(notas)
    return promedio

def ingresar_notas() -> list[float]:
    notas = []
    while True:
        entrada = input("Ingrese nota (s para salir): ")
        if entrada == "s":
            break
        nota = float(entrada)
        notas.append(nota)
    return notas
def mostrar_datos(promedio: float) -> None:
    print("**************")
    print(f"El promedio de las notas es: {promedio}")

def main():
    notas = ingresar_notas()
    promedio = promediar(notas)
    mostrar_datos(promedio)

main()
