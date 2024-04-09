"""
En la función de nuestro ejercicio hay un fallo potencial,
averigua cuándo sucede y retorna el valor None en ese caso especial,
en cualquier otro caso devuelve el resultado normal de la función.

def dividir(a, b):
    return a/b

Pista: Valor indeterminado
"""
def dividir(a, b):
    if b != 0:
        return a/b
    else:
        return None

print(dividir(1,0))

"""
Respuesta Profe:
"""
def dividir2(a, b):
    if b == 0:
        return None
    else:
        return a / b

resultado = dividir2(10, 0)
print(resultado)

try:
    x = float(input("Número: "))
    y = 2
    print(x / y)
except:
    print("Algo salió mal")