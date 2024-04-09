def dividir(numero_1: float, numero_2: float) -> float | bool:
    try:
        division = numero_1 / numero_2
        return division
    except ZeroDivisionError:
        print("No se puede dividir por cero.")
    except TypeError:
        print("Uno de los datos no es un número")
    except Exception as error:
        print(type(error))
    return False
def introducir_numeros() -> tuple[float, float]:
    while True:
        try:
            numero_1 = float(input("Número 1: "))
            numero_2 = float(input("Número 2: "))
        except ValueError:
            print("Uno de los datos no es un número. Vuelve a intentar")
            continue
        except KeyboardInterrupt:
            print("Sales del programa\n")
            exit()
        return numero_1, numero_2
def main():
    numero_1, numero_2 = introducir_numeros()
    division = dividir(numero_1, numero_2)
    if division:
        print(f"El resultado de la división es {division}")
    else:
        print("No pude realizar la division.")
    
main()