## Con type error (para saber el error)

def main():
    try:
        numero = input("Número: ")
        if numero == "":
            raise KeyboardInterrupt  # levantamos un error de forma manual
        x = 6 / int(numero)
        print(x)

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