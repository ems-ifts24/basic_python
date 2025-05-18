descripcion_ejercicio = "Stock de golosinas."
enunciado_completo = """Ejercicio 9:
Se ingresa por teclado la cantidad caramelos, chicles y chupetines disponibles en un kiosco (3 unidades) y sus nombres.
a. Determinar cuántos grupos de golosinas tienen más de 50 unidades.
   Mostrar en pantalla los nombres y las cantidades respectivas.
b. Sumar las cantidades mayores a 50 y hallar la incidencia sobre el total.
c. Si alguna de las cantidades es menor a 10, imprimir mensaje de verificación de stock."""

if input("¿Mostrar enunciado completo? (S para sí): ").upper() == "S":
    print(enunciado_completo)

print()
productos = []

for i in range(3):
    nombre = input(f"Ingrese el nombre del producto {i+1}: ")
    while True:
        try:
            cantidad = int(input(f"Ingrese la cantidad de {nombre}: "))
            productos.append((nombre, cantidad))    # Se guarda como una tupla
            break
        except ValueError:
            print("Error: debe ingresar un número entero.")

total = sum(c for _, c in productos)    # Se suman las cantidades de todas las golosinas 'c', sin considerar los nombres '_'

# Se utiliza la comprensión de listas para crear la nueva lista, tomando cada tupla (n nombre, c cantidad) de productos' y se verifica si la cantidad 'c' es mayor a 50.
# Forma general: [nueva_forma for cada_elemento in colección if condición]
mayores_50 = [(n, c) for n, c in productos if c > 50]
if mayores_50:
    print("\nProductos con más de 50 unidades:")
    for n, c in mayores_50:
        print(f"{n}: {c}")
    suma = sum(c for _, c in mayores_50)    # Se suman solo las golosinas con cantidad mayores a 50
    # En este contexto, la incidencia se refiere a cuánto representan las cantidades mayores a 50 unidades respecto del total general de productos, expresado en porcentaje
    print(f"Incidencia sobre el total: {suma / total * 100:.2f}%")

for nombre, cantidad in productos:
    if cantidad < 10:
        print(f"¡Atención! Verificar stock de {nombre} (cantidad: {cantidad})")
