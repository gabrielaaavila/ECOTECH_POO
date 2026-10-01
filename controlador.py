from modelo import AdministradorRRHH, UsuarioComun, ListaUsuarios, ServicioInformes

class ControladorRRHH:
    def __init__(self):
        self.usuarios = ListaUsuarios()
        self.admin = self.usuarios.usuarios[0]   # Administrador por defecto
        self.usuario_comun = self.usuarios.usuarios[1]

    # --- Control de empleados ---
    def crear_empleado(self, nombre, direccion, telefono, email, fecha_inicio_contrato, salario):
        try:
            self.admin.crear_empleado(nombre, direccion, telefono, email, fecha_inicio_contrato, salario)
            print(f"Empleado {nombre} creado correctamente.")
        except Exception as e:
            print("Error al crear empleado:", e)

    def ver_empleado(self, id_empleado):
        try:
            empleado = self.admin.ver_empleado(id_empleado)
            print("Datos del empleado:", empleado)
            return empleado
        except Exception as e:
            print("Error al consultar empleado:", e)

    def actualizar_empleado(self, id_empleado, nombre, direccion, telefono, email, fecha_inicio_contrato, salario):
        try:
            self.admin.actualizar_empleado(id_empleado, nombre, direccion, telefono, email, fecha_inicio_contrato, salario)
            print(f"Empleado {id_empleado} actualizado correctamente.")
        except Exception as e:
            print("Error al actualizar empleado:", e)

    def eliminar_empleado(self, id_empleado):
        try:
            self.admin.eliminar_empleado(id_empleado)
            print(f"Empleado {id_empleado} eliminado correctamente.")
        except Exception as e:
            print("Error al eliminar empleado:", e)

    # --- Control de departamentos ---
    def crear_departamento(self, nombre):
        self.admin.crear_departamento(nombre)
        print(f"Departamento {nombre} creado.")

    def ver_departamento(self, id_departamento):
        return self.admin.ver_departamento(id_departamento)

    def actualizar_departamento(self, id_departamento, nombre):
        self.admin.actualizar_departamento(id_departamento, nombre)
        print(f"Departamento {id_departamento} actualizado.")

    def eliminar_departamento(self, id_departamento):
        self.admin.eliminar_departamento(id_departamento)
        print(f"Departamento {id_departamento} eliminado.")

    # --- Control de proyectos ---
    def crear_proyecto(self, nombre, descripcion, fecha_inicio):
        self.admin.crear_proyecto(nombre, descripcion, fecha_inicio, None)
        print(f"Proyecto {nombre} creado.")

    def ver_proyecto(self, id_proyecto):
        return self.admin.ver_proyecto(id_proyecto)

    def actualizar_proyecto(self, id_proyecto, nombre):
        self.admin.actualizar_proyecto(id_proyecto, nombre)
        print(f"Proyecto {id_proyecto} actualizado.")

    # --- Control de registros de horas (usuario común) ---
    def registrar_horas(self, fecha, horas, descripcion, proyecto):
        self.usuario_comun.registrar_horas(fecha, horas, descripcion, proyecto)
        print("Horas registradas correctamente.")

    # --- Informes ---
    def generar_informe(self, tabla):
        servicio = ServicioInformes()
        servicio.generar_informe(tabla)
        print(f"Informe de {tabla} generado en Excel.")
