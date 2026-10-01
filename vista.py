from controlador import ControladorRRHH

def menu():
    print("\n--- Sistema de Gestión RRHH ---")
    print("1. Crear empleado")
    print("2. Ver empleado")
    print("3. Actualizar empleado")
    print("4. Eliminar empleado")
    print("5. Crear departamento")
    print("6. Crear proyecto")
    print("7. Registrar horas")
    print("8. Generar informe")
    print("0. Salir")

if __name__ == "__main__":
    controlador = ControladorRRHH()
    opcion = -1

    while opcion != 0:
        menu()
        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            print("Debe ingresar un número válido.")
            continue

        if opcion == 1:
            nombre = input("Nombre: ")
            direccion = input("Dirección: ")
            telefono = input("Teléfono: ")
            email = input("Email: ")
            fecha = input("Fecha inicio contrato (YYYY-MM-DD): ")
            salario = float(input("Salario: "))
            controlador.crear_empleado(nombre, direccion, telefono, email, fecha, salario)

        elif opcion == 2:
            id_empleado = int(input("ID empleado: "))
            controlador.ver_empleado(id_empleado)

        elif opcion == 3:
            id_empleado = int(input("ID empleado: "))
            nombre = input("Nombre: ")
            direccion = input("Dirección: ")
            telefono = input("Teléfono: ")
            email = input("Email: ")
            fecha = input("Fecha inicio contrato (YYYY-MM-DD): ")
            salario = float(input("Salario: "))
            controlador.actualizar_empleado(id_empleado, nombre, direccion, telefono, email, fecha, salario)

        elif opcion == 4:
            id_empleado = int(input("ID empleado: "))
            controlador.eliminar_empleado(id_empleado)

        elif opcion == 5:
            nombre = input("Nombre departamento: ")
            controlador.crear_departamento(nombre)

        elif opcion == 6:
            nombre = input("Nombre proyecto: ")
            descripcion = input("Descripción: ")
            fecha = input("Fecha inicio (YYYY-MM-DD): ")
            controlador.crear_proyecto(nombre, descripcion, fecha)

        elif opcion == 7:
            fecha = input("Fecha (YYYY-MM-DD): ")
            horas = float(input("Horas trabajadas: "))
            descripcion = input("Descripción tarea: ")
            proyecto = input("Proyecto: ")
            controlador.registrar_horas(fecha, horas, descripcion, proyecto)

        elif opcion == 8:
            tabla = input("Tabla para informe (empleado/departamento/proyecto): ")
            controlador.generar_informe(tabla)

        elif opcion == 0:
            print("Saliendo del sistema...")
        else:
            print("Opción no válida.")
