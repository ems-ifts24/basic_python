descripcion_ejercicio = "Promedio de tres números."
enunciado_completo = """Ejercicio 1:
Ingresar tres números. Calcular su promedio. Si es mayor a 10, mostrarlo.
En ambos casos, calcular las diferencias entre cada número y el promedio."""

if input("¿Mostrar enunciado completo? (S para sí): ").upper() == "S":
    print(enunciado_completo)

print()
numeros = []
while len(numeros) < 3:
    try:
        num = float(input(f"Ingrese el número {len(numeros)+1}: "))
        numeros.append(num)
    except ValueError:
        print()
        print("Debe ingresar un número")

promedio = sum(numeros) / 3

if promedio > 10:
    print()
    print(f"El promedio es mayor a 10: {promedio:.2f}")

print()
for i, num in enumerate(numeros):
    diferencia = num - promedio
    print(f"Diferencia entre número {i+1} y el promedio: {diferencia:.2f}")
