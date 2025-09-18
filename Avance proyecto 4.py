cursos = []

def agregar_curso():
    nombre = input("Nombre del curso: ")
    if nombre == "":
        print("¡Debes escribir un nombre!\n")
        return
    try:
        nota = float(input("Nota (0 a 100): "))
        if nota < 0 or nota > 100:
            print("¡La nota debe estar entre 0 y 100!\n")
            return
    except:
        print("¡Eso no es un número!\n")
        return
    cursos.append([nombre, nota])
    print(f"Curso '{nombre}' guardado con nota {nota}\n")

def ver_cursos():
    if len(cursos) == 0:
        print("No tienes cursos todavía\n")
    else:
        for i in range(len(cursos)):
            print(f"{i+1}. {cursos[i][0]}: {cursos[i][1]}")
    print()

def calcular_promedio():
    if len(cursos) == 0:
        print("No tienes cursos para calcular promedio\n")
    else:
        total = 0
        for curso in cursos:
            total += curso[1]
        promedio = total / len(cursos)
        print(f"Tu promedio es: {promedio:.1f}\n")

def buscar_curso():
    if len(cursos) == 0:
        print("No tienes cursos para buscar\n")
        return
    buscar = input("Nombre del curso a buscar: ")
    for curso in cursos:
        if curso[0].lower() == buscar.lower():
            print(f"Encontrado: {curso[0]} - Nota: {curso[1]}\n")
            return
    print("No se encontró ese curso\n")

def eliminar_curso():
    if len(cursos) == 0:
        print("No hay cursos para eliminar\n")
        return
    eliminar = input("Nombre del curso a eliminar: ")
    for i in range(len(cursos)):
        if cursos[i][0].lower() == eliminar.lower():
            cursos.pop(i)
            print(f"Curso '{eliminar}' eliminado\n")
            return
    print("No se encontró ese curso\n")

while True:
    print("1. Agregar curso")
    print("2. Ver cursos")
    print("3. Calcular promedio")
    print("4. Buscar curso")
    print("5. Eliminar curso")
    print("6. Salir")
    opcion = input("Elige una opción: ")
    print()
    if opcion == "1":
        agregar_curso()
    elif opcion == "2":
        ver_cursos()
    elif opcion == "3":
        calcular_promedio()
    elif opcion == "4":
        buscar_curso()
    elif opcion == "5":
        eliminar_curso()
    elif opcion == "6":
        print("¡Chao!")
        break
    else:
        print("Opción no válida\n")