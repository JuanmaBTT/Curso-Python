
def ingreso_de_datos ():
    while True:
        año = input ("INGRESE UN AÑO: ")
        if  año.isdigit():
            return int (año)
        else:
            print ("Ingrese un número")
        
def año_bisiesto (año):
    if (año % 4 == 0) and (año % 100 !=0):
        resultado = f"EL AÑO {año} ES BISIESTO"
    elif (año % 400 == 0):
        resultado = f"EL AÑO {año} ES BISIESTO"
    else: 
        resultado = f"EL AÑO {año} NO ES BISIESTO"      
    return resultado

def main ():
    año= ingreso_de_datos()
    resultado = año_bisiesto(año)
    print (resultado)

main()
