"""
Tomando la solución del ejercicio pasado, en lugar de devolver None al dividir entre cero,
tienes que capturar una excepciión que muestre por pantalla el mensaje:
"No se puede dividir por cero" Además, capturar otros posibles errores.

def dividir(a, b):
    if b == 0:
        return None
    else:
        return a / b
resultado = dividir(10, 0)
print(resultado)
"""

def main():            
    try:
        a = input("Número a: ")
        b = input("Número b: ")
        if b == "":
            raise KeyboardInterrupt  # levantamos un error de forma manual
        division = int(a) / int(b)
        print(division)

    except ValueError:
        print("Debes introducir números, no caracteres que no lo sean")
    except TypeError:
        print("No se puede divir el número y una cadena")
    except NameError:
        print("Hay un problema con el código, no existe alguna variable")
    except ZeroDivisionError:
        print("No se puede dividir por cero")
    except KeyboardInterrupt:
        print("\n Acabas de salir del programa")
        return
    except Exception as error:
        print("Ha ocurrido un error:", type(error))

main()