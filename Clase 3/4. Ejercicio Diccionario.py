"""""
Solicitar al usuario el nombre de un producto,
luego su precio.
El programa deberá agregar un impuesto sobre el precio del producto.
Crear un diccionario con las siguientes claves:
    "producto": nombre del producto
    "precio": precio del producto
Finalmente, mostrar un mensaje con el siguiente formato:
    El producto {producto} tiene un precio de {precio}.
"""
producto = (input("¿Cual es el producto?"))
precio_sin_iva = float(input(f'¿Cual es el precio del {producto}?'))

print(f'El producto {producto} tiene un precio de {precio_sin_iva}')
precio_producto = (precio_sin_iva*1.22)

print(f'El producto {producto} tiene un precio de {precio_producto}')
