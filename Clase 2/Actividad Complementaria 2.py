#Identifica el tipo de dato (int, float, string, list o touple) de los siguientes valores literales.


#Dato y Tipo de datos
"""
"Hola Mundo" = str
[1, 10, 100] =list
-25 = int
(8, 100, -12) = tuple
1.167 = float 
["Hola", "Mundo"] = list
' ' = str
(1, -5, "Hola!") = tuple
"""
#2) Determina mentalmente (sin programar) el resultado que aparecerá por pantalla a partir de las siguientes variables:

a :int = 10
b :int = -5
c : str = "Hola"
d : list = [1, 2, 3]
e : tuple = (4,5,6)

# Ejecutar y Resultado
print(a * 5)  
print(a - b) 
print(c + "Mundo")
print(c * 2)
print(c[-1])
print(c[1:])
print(d + d)
print(e[1])
print(e+(7,8,9))

"""3) El siguiente código pretende realizar una media entre 3 números, pero no funciona correctamente. ¿Eres capaz de identificar el problema y solucionarlo?

In [1]:
numero_1 = 9
numero_2 = 3
numero_3 = 6
​
media = numero_1 + numero_2 + numero_3 / 3
print("La nota media es", media)
La nota media es 14.0 """
numero_1 = 9
numero_2 = 3
numero_3 = 6

media = (numero_1 + numero_2 + numero_3) / 3
print("La nota media es", media)

"""4) A partir del ejercicio anterior, desarrolla un programa para calcular la nota final. Para ello vamos a suponer que cada número es una nota y que queremos obtener la nota media. Cada nota tiene un valor porcentual:

La primera nota vale un 15% del total
La segunda nota vale un 35% del total
La tercera nota vale un 50% del total
Ejemplos:
nota_1 = 10
nota_2 = 7
nota_3 = 4"""

PRIMERA_NOTA=0.15
SEGUNDA_NOTA=0.35
TERCERA_NOTA=0.5

nota_1 = 10
nota_2 = 7
nota_3 = 4

nota_final=PRIMERA_NOTA*nota_1+SEGUNDA_NOTA*nota_2+TERCERA_NOTA*nota_3
print(nota_final)

"""
5) La siguiente matriz (o lista con listas anidadas) debe cumplir una condición: en cada fila el cuarto elemento siempre debe ser el resultado de sumar los tres primeros. ¿Eres capaz de modificar las sumas incorrectas utilizando la técnica del slicing?


🖐 Ayuda:  La función llamada sum(lista) devuelve una suma de todos los elementos de la lista

Partirás de: 
matriz = [ 
    [1, 5, 1],
    [2, 1, 2],
    [3, 0, 1],
    [1, 4, 4]
]
Debes llegar a: 
matriz = [ 
    [1, 5, 1, 7],
    [2, 1, 2, 5],
    [3, 0, 1, 4],
    [1, 4, 4, 9]
]

"""
matriz = [ 
    [1, 5, 1],
    [2, 1, 2],
    [3, 0, 1],
    [1, 4, 4]
]
matriz[0]=matriz[0]+[sum(matriz[0])]

matriz[1]=matriz[1]+[sum(matriz[1])]

matriz[2]=matriz[2]+[sum(matriz[2])]

matriz[3]=matriz[3]+[sum(matriz[3])]

from pprint import pprint

pprint(matriz, width=20)