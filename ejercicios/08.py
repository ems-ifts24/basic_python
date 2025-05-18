descripcion_ejercicio = "División, curso y beca según nota y edad de dos alumnos."
enunciado_completo = """Ejercicio 8:
Diseñar un algoritmo para determinar el ingreso de dos alumnos a una academia de inglés;
se ingresan por teclado las notas de los exámenes nivelatorios y las edades de los alumnos.
a. Si aprobó el examen, va a la división “A”; sino, a la división “B”.
b. Curso 1: hasta 10 años. Curso 2: de 10 a 20. Curso 3: más de 20.
c. Si el alumno aprobó con 9 ó 10, se le otorgan Becas."""

if input("¿Mostrar enunciado completo? (S para sí): ").upper() == "S":
    print(enunciado_completo)

print()
for i in range(1, 3):
    while True:
        try:
            print(f"\nAlumno {i}:")
            nota = int(input("Ingrese la nota del examen nivelatorio: "))
            if nota < 1 or nota > 10:
                print("Error: la nota debe estar entre 1 y 10.")
                continue # reinicia el ciclo while si no se cumple la condicion

            edad = int(input("Ingrese la edad del alumno: "))
            if edad < 5:
                print("Error: el alumno debe tener al menos 5 años.")
                continue # reinicia el ciclo while si no se cumple la condicion

            division = "A" if nota >= 6 else "B"
            print(f"División: {division}")

            if edad <= 10:
                print("Curso: CURSO 1")
            elif edad <= 20:
                print("Curso: CURSO 2")
            else:
                print("Curso: CURSO 3")

            if nota >= 9:
                print("¡Se le otorga una beca!")
            break # termina el ciclo while y continuar con el siguiente ciclo del for
        except ValueError:
            print("Error: debe ingresar números válidos. Inténtelo nuevamente.")
