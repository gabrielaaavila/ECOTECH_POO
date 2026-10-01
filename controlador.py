import modelo

##login
def validar_usuario(username, password):
    usuarios = modelo.ListaUsuarios()
    usuarios = usuarios.usuarios
    for usuario in usuarios:
        if usuario.username == username and usuario.password == password:
            return usuario
    print("Login fallido")
    return False

def agregar_empleado(usuario):
    nombre = input("Ingrese nombre: ")
    direccion = input("Ingrese direccion: ")
    telefono = input("Ingrese telefono: ")
    email = input("Ingrese email: ")
    fecha_inicio_contrato = input("Ingrese fecha de inicio de contrato: ")
    salario = input("Ingrese salario")
    usuario.crear_empleado(nombre, direccion, telefono, email, fecha_inicio_contrato, salario)