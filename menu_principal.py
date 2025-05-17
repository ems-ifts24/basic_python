import os

def cargar_ejercicios():
    ejercicios = []
    print("Ingrese los números de ejercicios a incluir en el menú (01 al 99).")
    print("Ingrese 00 para finalizar la carga. Máximo 10 ejercicios.")
    
    while len(ejercicios) < 10:
        entrada = input(f"Ejercicio {len(ejercicios)+1}: ").zfill(2)

        if entrada == "00":
            break
        elif not entrada.isdigit() or not (1 <= int(entrada) <= 99):
            print("Dato inválido. Debe ser un número entre 01 y 99. Para finalizar, ingrese 00.")
        elif entrada in ejercicios:
            print("Ya fue ingresado ese ejercicio.")
        else:
            ejercicios.append(entrada.zfill(2))
    
    return ejercicios


def mostrar_menu(ejercicios):
    print("\n=== MENÚ DE EJERCICIOS ===")
    print("0. Salir")
    for i, ejercicio in enumerate(ejercicios, start=1):
        nombre = obtener_descripcion_ejercicio(ejercicio)
        print(f"{i}. Ejercicio {ejercicio}: {nombre}")


def obtener_descripcion_ejercicio(numero):
    try:
        with open(f"./ejercicios/{numero}.py", encoding="utf-8") as f:
            for line in f:
                if line.startswith("descripcion_ejercicio"):
                    return line.split("=")[1].strip().strip('"').strip("'")
        return "Descripción no encontrada"
    except FileNotFoundError:
        return "Archivo no encontrado"


def ejecutar_ejercicio(ejercicio):
    ruta = f"./ejercicios/{ejercicio}.py"
    if os.path.isfile(ruta):
        os.system(f"python {ruta}")
    else:
        print(f"El archivo {ruta} no existe.")


def main():
    ejercicios = cargar_ejercicios()
    if not ejercicios:
        print("No se ingresaron ejercicios. Finalizando.")
        return

    while True:
        mostrar_menu(ejercicios)
        opcion = input("Seleccione una opción: ")
        
        if opcion == "0":
            print("Saliendo del programa.")
            break
        elif opcion.isdigit() and 1 <= int(opcion) <= len(ejercicios):
            ejercicio = ejercicios[int(opcion) - 1]
            ejecutar_ejercicio(ejercicio)
        else:
            print("Opción inválida. Intente nuevamente.")

# Se define el punto de entrada del script cuando se ejecuta directamente
if __name__ == "__main__":
    main()
