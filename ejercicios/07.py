descripcion_ejercicio = "Calcular totales de compra y aplicar descuento si > $100."
enunciado_completo = """Ejercicio 7:
Diseñar un programa que, al ingresar por teclado el precio por kilo y
la cantidad en kilos adquirida por un cliente de tres productos (6 variables), muestre:
a. El monto total en pesos correspondiente a la compra de cada producto.
b. El total en pesos de la compra realizada por el cliente.
c. Si el total es superior a $100, hacer un descuento del 10%. Mostrar el nuevo monto."""

if input("¿Mostrar enunciado completo? (S para sí): ").upper() == "S":
    print(enunciado_completo)

print()
descuento = 0.10
total = 0
for i in range(1, 4):
    while True:
        try:
            precio = float(input(f"Producto {i} - Ingrese precio por kilo: "))
            kilos = float(input(f"Producto {i} - Ingrese cantidad en kilos: "))
            if precio < 0 or kilos < 0:
                raise ValueError()
            subtotal = precio * kilos
            print(f"Total producto {i}: ${subtotal:.2f}")
            total += subtotal
            break
        except ValueError:
            print("Error: Solo se permiten números positivos. Inténtelo de nuevo.")

print(f"\nTotal de la compra: ${total:.2f}")
if total > 100:
    descuento *= total
    print(f"Se aplica un 10% de descuento: ${descuento:.2f}")
    print(f"Total con descuento: ${total - descuento:.2f}")
