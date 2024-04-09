"""
Realiza una función llamada recortar() que reciba tres parámetros. El primero es el número a recortar, 
el segundo es el límite inferior y el tercero el límite superior. La función tendrá que cumplir lo siguiente:

Devolver el límite inferior si el número es menor que éste
Devolver el límite superior si el número es mayor que éste.
Devolver el número sin cambios si no se supera ningún límite.
Comprueba el resultado de recortar 15 entre los límites 0 y 10

"""
a=15
b=0
c=10

def recortar(a,b,c):
    "El primero es el número a recortar, el segundo es el límite inferior y el tercero el límite superior."
    if a<b:
        return b
    elif a>c:
        return c
    elif a>b and a<c:
        return a

def resultado (result,a,b,c):
    if result==b:
        print(f'El resultado es {b}.')
    elif result==c:
        print(f'El resultado es {c}.')
    if result==a:
        print(f'El resultado es {a}.')

def main():
    result=recortar(a,b,c)
    resultado(result,a,b,c)

main()
