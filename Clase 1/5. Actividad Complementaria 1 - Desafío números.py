"""""Actividad 1 - Mi primer programa en Python:

Trabajas en Coderhouse y te piden crear un programa que calcule la nota final de estudiantes del curso de Python. La nota final se calcula basándonos en tres notas previas de las cuales, cada una corresponde un porcentaje distinto de la nota final. Los porcentajes se detallan a continuación:  
Los porcentajes asociados que debemos considerar de cada nota se detallan a continuación: 
nota_1  cuenta como el 20% de la nota final
nota_2 cuenta como el 30% de la nota final
nota_3 cuenta como el 50% de la nota final
"""
ponderacion_resultado1 = 0.2
ponderacion_resultado2 = 0.3
ponderacion_resultado3 = 0.5

numero_1 = input ("Nota N° 1: ")
numero_1= int (numero_1)
numero_2= input ("Nota N° 2: ")
numero_2= int (numero_2)
numero_3= input ("Nota N° 3: ")
numero_3= int (numero_3)
resultado = ponderacion_resultado1* numero_1 + ponderacion_resultado2*numero_2 + ponderacion_resultado3*numero_3
print ("Nota Final Estudiante: ", resultado)