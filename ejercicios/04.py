descripcion_ejercicio = "Verificar si I/J = K/L, evitando división por cero."
enunciado_completo = """Ejercicio 4:
Diseñar un algoritmo que ingrese I, J, K y L. Si I/J = K/L imprimir “Si, son
iguales”. Caso contrario no dar mensaje. Verificar que los divisores sean distintos de cero."""

if input("¿Mostrar enunciado completo? (S para sí): ").upper() == "S":
    print(enunciado_completo)

print()
numeros = []
letras = ["I", "J", "K", "L"]
for i in range(len(letras)):
    while True:
        try:
            num = float(input(f"Ingrese {letras[i]}: "))
            numeros.append(num)
            break
        except ValueError:
            print("Error: Debe ingresar un número. Inténtelo de nuevo.")

# Verificar divisores distintos de cero
if numeros[1] == 0:
    print("Error: J no puede ser cero.")
elif numeros[3] == 0:
    print("Error: L no puede ser cero.")
else:
    # Calcular I/J = K/L
    if numeros[0] / numeros[1] == numeros[2] / numeros[3]:
        print("Sí, son iguales.")