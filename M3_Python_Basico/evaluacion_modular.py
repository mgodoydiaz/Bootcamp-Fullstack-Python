"""
Evaluación Modular 3
Miguel Godoy Díaz
18.720.297-3

Trabaja Python simple, definición de funciones, ciclos y estructuras simples para 
almacenar información de horas médicas.

Todo dentro de la Memoria RAM, sin crear archivos para mantener la información en el disco.
"""

# Lista que almacena todas las horas médicas
horas = []  # Se trabajará como parámetro global

# Función para registrar una hora médica
def registrar_hora():
    print("\nRegistro de nueva hora")
    hora = {
        "rut": input("RUT del paciente: "),
        "nombre": input("Nombre completo: "),
        "direccion": input("Dirección: "),
        "edad": input("Edad: "), 
        # Se deja como string, no hay necesidad de verificarlo ni hacer operaciones 
        "comuna": input("Comuna: "),
        "celular": input("Número de celular: "),
        "correo": input("Correo: "),
        "prevision": input("Previsión (Fonasa, Isapre, FFAA, Otra): "),
        "fecha": input("Fecha (dd-mm-aaaa): "),
        "hora": input("Hora (hh:mm): ")
    }
    horas.append(hora)
    print("Hora registrada correctamente")
    return None 

# Función para listar todas las horas
def listar_horas():
    if not horas: # Lista vacía
        print("No hay horas registradas")
        return

    for h in horas:
        print("\nPaciente:", h["nombre"])
        for clave, valor in h.items():
            print(clave, ":", valor)

# Función para buscar una hora por RUT
def buscar_hora():
    rut = input("Ingrese RUT a buscar: ")
    for h in horas:
        if h["rut"] == rut:
            print("\nDatos del paciente")
            for clave, valor in h.items():
                print(clave, ":", valor)
            return
    print("Paciente no encontrado")

# Función para eliminar una hora por RUT
def eliminar_hora():
    rut = input("Ingrese RUT a eliminar: ")
    for i, h in enumerate(horas):
        if h["rut"] == rut:
            horas.pop(i)
            print("Hora eliminada correctamente")
            return
    print("Paciente no encontrado")

# Función para modificar una hora por RUT
def modificar_hora():
    rut = input("Ingrese RUT a modificar: ")
    for h in horas:
        if h["rut"] == rut:
            print("Modificar datos (deje vacío para mantener)")
            for clave in h:
                nuevo = input(f"{clave}: ")
                if nuevo != "":
                    h[clave] = nuevo
            print("Hora modificada correctamente")
            return
    print("Paciente no encontrado")

# Menú principal
while True:
    print("\nCLÍNICA DOCTOR PYTHON")
    print("1. Ingresar hora")
    print("2. Listar horas")
    print("3. Eliminar hora")
    print("4. Modificar hora")
    print("5. Buscar hora")
    print("6. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        registrar_hora()
    elif opcion == "2":
        listar_horas()
    elif opcion == "3":
        eliminar_hora()
    elif opcion == "4":
        modificar_hora()
    elif opcion == "5":
        buscar_hora()
    elif opcion == "6":
        print("Usted ha salido del sistema, hasta pronto")
        break
    else:
        print("Opción inválida")
