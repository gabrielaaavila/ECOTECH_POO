import modelo
import controlador

while True:
    #login
    usuario = False
    while usuario == False:
        username = input("Ingrese su usuario: ")
        password = input("Ingrese su contraseña: ")
        usuario = controlador.validar_usuario(username, password)

    print("Hola", username)
    if usuario.tipo_usuario == "administrador": #si se logea como admin
        menu = print("""Qué desea gestionar?
1. Empleado
2. Departamento
3. Proyecto""")
        opcion = input("ingrese una opcion: ")
        if opcion == "1":   #si elige empleado
            menu = ("""qué desea hacer?
1. Agregar empleado
2. Actualizar empleado
3. Eliminar empleado
4. Generar informe""")
            opcion = input("ingrese una opcion: ")
            if opcion == "1": #si elige agregar empleado
                controlador.agregar_empleado(usuario)
                print("Empleado agregado con éxito")
            if opcion == "2": #si elige actualizar empleado
                pass
            if opcion == "3": #si elige eliminar empleado
                pass
            if opcion == "4": #si elige generar informe
                pass

        elif opcion == "2": #si elige departamento
            pass
        elif opcion == "3": # si elige proyecto
            pass

    elif usuario.tipo_usuario == "comun": #si se logea como usuario comun
        menu = print("""Qué desea hacer?
1. Registrar horas""")