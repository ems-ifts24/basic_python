descripcion_ejercicio = "Verificar si alcanzan los bancos para los alumnos. Informar faltantes."
enunciado_completo = """Ejercicio 5:
Sabiendo la cantidad de bancos de un aula, y la cantidad de alumnos
inscriptos para ese curso, determinar si alcanzan los bancos existentes.
De no ser así, informar además cuántos bancos sería necesario agregar."""

if input("¿Mostrar enunciado completo? (S para sí): ").upper() == "S":
    print(enunciado_completo)

MSG_ERROR = "Error: debe ingresar números enteros positivos. Inténtelo de nuevo."

print()
while True:
    try:
        bancos = int(input("Ingrese la cantidad de bancos: "))
        alumnos = int(input("Ingrese la cantidad de alumnos: "))

        if bancos < 0 or alumnos < 0:
            raise ValueError(MSG_ERROR)

        if bancos >= alumnos:
            print("Los bancos alcanzan. ")
        else:
            diferencia = alumnos - bancos
            print(f"No alcanzan los bancos. {'Falta' if diferencia == 1 else 'Faltan'} {alumnos - bancos} {'banco' if alumnos - bancos == 1 else 'bancos'}.")
        break   # salida del while
    except ValueError:
        print(MSG_ERROR)

