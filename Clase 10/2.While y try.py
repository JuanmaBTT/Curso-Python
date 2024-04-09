while True:
    try:
        a = float(input("Número 1: "))
        b = float(input("Número 2: "))
    except:
        print("Ha ocurrido un error. Tienes que introducir 2 números")
    else:
        print(a + b)
        break

### Con Finally (siempre se ejecuta)
    
while True:
    try:
        a = float(input("Número 1: "))
        b = float(input("Número 2: "))
    except:
        print("Ha ocurrido un error. Tienes que introducir 2 números")
    else:  # opcional
        print(a + b)
        break
    finally:  # opcional
        print("Siempre se ejecuta")

