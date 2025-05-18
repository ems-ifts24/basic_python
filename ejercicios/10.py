descripcion_ejercicio = "Catálogo de cuadros: verificar antigüedad y renovar si necesario."
enunciado_completo = """Ejercicio 10:
Una galería de arte desea preparar un catálogo de sus cuadros más famosos.
Se realiza una prueba con tres cuadros y para cada uno se ingresa el nombre y el año.
a. Verificar si todos los cuadros son anteriores al siglo XX.
b. Determinar cuántos tienen antigüedad inferior a 10 años.
   Si no hay ninguno, imprimir “renovar stock”."""

if input("¿Mostrar enunciado completo? (S para sí): ").upper() == "S":
    print(enunciado_completo)

print()
from datetime import datetime
anio_actual = datetime.now().year

cuadros = []
cantidad_cuadros = 3
recientes = 0
anteriores_siglo_20 = True

for i in range(cantidad_cuadros):
    nombre = input(f"Ingrese nombre del cuadro {i+1}: ")
    while True:
        try:
            anio = int(input(f"Ingrese año de creación de {nombre}: "))
            if anio > anio_actual:
                print(f"Error: el año no puede ser mayor a {anio_actual}. Inténtelo de nuevo.")
                continue

            cuadros.append((nombre, anio))

            if anio >= 1901:
                anteriores_siglo_20 = False
            if anio_actual - anio < 10:
                recientes += 1
            break
        except ValueError:
            print("Error: debe ingresar un año válido.")

if anteriores_siglo_20:
    print("Todos los cuadros son anteriores al siglo XX.")
if recientes == 0:
    print("Renovar stock.")
