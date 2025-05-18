descripcion_ejercicio = "Área de triángulo con base y altura igual al cuadrado de la base."
enunciado_completo = """Ejercicio 2:
Calcular el área de un triángulo, conociendo la base, y sabiendo que su
altura es igual al cuadrado de la base."""

if input("¿Mostrar enunciado completo? (S para sí): ").upper() == "S":
    print(enunciado_completo)

print()
numeros = []
while len(numeros) < 3:
    try:
        base = float(input("Ingrese la base del triángulo: "))
    except ValueError:
        print()
        print("Debe ingresar un número")

altura = base ** 2
area = (base * altura) / 2

print(f"Altura calculada: {altura:.2f}")
print(f"Área del triángulo: {area:.2f}")
