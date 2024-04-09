"""
6) Utilizando la función range() y la conversión a listas, genera las siguientes listas dinámicamente:
Todos los números del 0 al 10 [0, 1, 2, ..., 10]
Todos los números del -10 al 0 [-10, -9, -8, ..., 0]
Todos los números pares del 0 al 20 [0, 2, 4, ..., 20]
Todos los números impares entre -20 y 0 [-19, -17, -15, ..., -1]
Todos los números múltiples de 5 del 0 al 50 [0, 5, 10, ..., 50]
🖐 Ayuda: la conversión de listas es mi_lista=list(range(inicio,fin,salto))
"""
lista_0_al_10=[]
for i in range(0,11):
      lista_0_al_10.append(i)
print(lista_0_al_10)

lista_menos_10_al_0=[]

for i in range(-10,1):
      lista_menos_10_al_0.append(i)
print(lista_menos_10_al_0)

lista_0_al_20_pares=[]
for i in range(0,21,2):
      lista_0_al_20_pares.append(i)
print(lista_0_al_20_pares)

lista_menos_20_al_0_impares=[]

for i in range(-19,1,2):
      lista_menos_20_al_0_impares.append(i)
print(lista_menos_20_al_0_impares)

lista_0_al_50_mltiplo_5=[]
for i in range(0,51,5):
      lista_0_al_50_mltiplo_5.append(i)
print(lista_0_al_50_mltiplo_5)