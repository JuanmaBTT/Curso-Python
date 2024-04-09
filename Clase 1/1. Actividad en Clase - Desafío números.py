""" Actividad en Clase: Desafío números.

Descripción de acividad individual:

En nuestro trabajo nos solicitan desarrollar un programa que permita calcular el promedio final de los equipos de fútbol en un torne. Para ello, debemos considerar tres aspectos:
1) Jugaron 20 partidos durante el torneo.
2) Los partidos poseen diferente puntaje según el resultado, los partidos ganados 3 puntos, partido empatado 1 punto y perdido 0 punto.
3) El promedio final resulta de la cantidad de puntos totales divididos la cantidad de partidos"""

cantidad_de_partidos = int(input ("Cantidad de Partidos: "))
partidos_ganados= int(input ("Cantidad de Partidos Ganados: "))
partidos_empatados= int(input ("Cantidad de Partidos Empatados: "))
partidos_perdidos= int(input ("Cantidad de Partidos Perdidos: "))
resultado = (3*partidos_ganados + 1*partidos_empatados + 0*partidos_perdidos)/cantidad_de_partidos
print ("Promedio Final: ", resultado)

#Otra forma de hacerla (Mejor)

# Declaración de datos
PUNTOS_PARTIDO_GANADO = 3
PUNTOS_PARTIDO_EMPATADO = 1
PUNTOS_PARTIDO_PERDIDO = 0
PARTIDOS_JUGADOS = 20

# Entrada de datos
partidos_ganados = int(input("¿Cuantos partidos ha ganado?: "))
partidos_perdidos = int(input("¿Cuantos partidos ha perdido?: "))
partidos_empatados = int(input("¿Cuantos partidos ha empatado?: "))

# Operaciones
puntos_totales = (
    partidos_ganados * PUNTOS_PARTIDO_GANADO
    + partidos_empatados * PUNTOS_PARTIDO_EMPATADO
    + partidos_perdidos * PUNTOS_PARTIDO_PERDIDO
)
promedio = puntos_totales / PARTIDOS_JUGADOS

# Salida de datos
print(f"El promedio final de puntos es {promedio}")