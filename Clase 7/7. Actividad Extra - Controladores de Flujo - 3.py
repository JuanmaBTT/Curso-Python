"""
3) Escribe un programa que sume todos los números enteros impares desde el 0 hasta el 100:

🖐 Ayuda: Puedes utilizar la funciones sum() y range() para hacerlo más fácil. El tercer parámetro en la función range(inicio, fin, salto) indica un salto de números.

"""
### 3) Escribe un programa que sume todos los números enteros impares desde el 0 hasta el 100:
###🖐 Ayuda: Puedes utilizar la funciones sum() y range() para hacerlo más fácil. 
### El tercer parámetro en la función range(inicio, fin, salto) indica un salto de números.

## Total del 0 al 100:
inicio_suma= 0
limite_suma = 101
suma = 0

for i in range(inicio_suma,limite_suma):
        suma+= i
print("La suma total es:", suma)

## Total del 0 al 100 impares:

inicio_suma= 0
limite_suma = 101
suma = 0

for i in range(inicio_suma,limite_suma):
    if i %2!=0:
        suma+= i
print("La suma total es:", suma)

inicio_suma= 1
limite_suma = 101
suma = 0

for i in range(inicio_suma,limite_suma,2):
        suma+= i
print("La suma total es:", suma)

## Total del 0 al 100 pares:

inicio_suma= 0
limite_suma = 101
suma = 0

for i in range(inicio_suma,limite_suma):
    if i %2==0:
        suma+= i
print("La suma total es:", suma)

inicio_suma= 0
limite_suma = 101
suma = 0

for i in range(inicio_suma,limite_suma,2):
        suma+= i
print("La suma total es:", suma)