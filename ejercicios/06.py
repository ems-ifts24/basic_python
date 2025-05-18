descripcion_ejercicio = "Raíz si el número es >= 0, raíz del módulo si es negativo."
enunciado_completo = """Ejercicio 6:
Ingresar un número. Si es positivo o cero, hallar su raíz. Si no,
hallar el módulo y luego la raíz de éste."""

import math

if input("¿Mostrar enunciado completo? (S para sí): ").upper() == "S":
    print(enunciado_completo)

print()

while True:
    try:
        numero = float(input("Ingrese un número: "))
        if numero >= 0:
            resultado = math.sqrt(numero)
            print(f"La raíz cuadrada es: {resultado:.2f}")
        else:
            resultado = math.sqrt(abs(numero))
            print(f"La raíz cuadrada es: {resultado:.2f}")
        break   # salida del while
    except ValueError as e:
        print("Error: debe ingresar un número.")
        print()