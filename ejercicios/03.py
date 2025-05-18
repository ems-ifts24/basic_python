descripcion_ejercicio = "Coeficientes de ecuación de segundo grado: determinar si las raíces son reales."
enunciado_completo = """Ejercicio 3:
Dados los coeficientes de la ecuación de segundo grado, determinar si las
raíces son reales. (Ayuda: verifique el valor del discriminante...)."""

if input("¿Mostrar enunciado completo? (S para sí): ").upper() == "S":
    print(enunciado_completo)

print()
numeros = []
while len(numeros) < 3:
    try:
        a = float(input("Ingrese coeficiente a: "))
        b = float(input("Ingrese coeficiente b: "))
        c = float(input("Ingrese coeficiente c: "))
    except ValueError:
        print()
        print("Debe ingresar un número")

discriminante = b**2 - 4*a*c

if discriminante > 0:
    print("Las raíces son reales y distintas.")
elif discriminante == 0:
    print("Las raíces son reales e iguales.")
else:
    print("Las raíces no son reales.")
