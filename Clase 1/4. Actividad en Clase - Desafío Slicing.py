""" Actividad en Clase: Desafío Slicing

Descripción de acividad individual:

Se tiene una cadena de texto, pero al revés. Al parecer contiene el nombre de un alumno, la nota de un examen y la materia

De forma individual, realiza lo siguiente:
1) Dar vuelta la cadena y asignarla a una variable llamada cadena_volteada. Para devolver una cadena dada vuelta se usa el tercer índice negativo con slicing: cadena [::-1]
2) Extraer nombre y apellido, almacenarlo en una variable llamada: nombre_alumno
3) Extraer la nota y almacenarla en una variable llamada nota.
4) Extraer la materia y almacenarla en una variable llamada materia.
5) Mostrar por pantalla la siguiente estructura:

NOMBRE APELLIDO ha sacado un NOTA en MATERIA

Formateando las anteriores variables en una variable llamada:
cadena_formateada
cadena = "acitametaM,5,8,otipeP ordeP"
Para formatear recuerde concatenar!
"""
cadena = "acitametaM,5,8,otipeP ordeP"
cadena_formateada = cadena[::-1]
nombre_alumno = cadena_formateada[0:12]
nota = cadena_formateada [13:16]
materia = cadena_formateada [17:]
resultado = str(nombre_alumno)+" ha sacado un "+str(nota)+" en "+str(materia)

print (cadena_formateada)
print (nombre_alumno)
print(nota)
print(materia)
print(resultado)