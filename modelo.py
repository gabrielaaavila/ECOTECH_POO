import sqlite3 
from pandas import DataFrame 

class Conexion:
    def ejecutar(query, valores):
            try:
                conn = sqlite3.connect('test.db') 
                c = conn.cursor()
                c.execute(query, valores)
                resultado = c.fetchall()
                conn.commit()
                conn.close()
                return resultado
            except sqlite3.Error as ex:
                print("Error en la conexión", ex)

class Usuario:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class ListaUsuarios:
    def __init__(self):
        self.usuarios = [AdministradorRRHH("admin", "admin"), UsuarioComun("usuario1", "1234")]

class AdministradorRRHH(Usuario):
    def __init__(self, username, password):
        super().__init__(username, password)
        self.tipo_usuario = "administrador"

    def crear_empleado(self, nombre, direccion, telefono, email, fecha_inicio_contrato, salario):
        query = "INSERT INTO empleado (nombre, direccion, telefono, email, fecha_inicio_contrato, salario) VALUES (?, ?, ?, ?, ?, ?)"
        valores = (nombre, direccion, telefono, email, fecha_inicio_contrato, salario)
        Conexion.ejecutar(query, valores)

    def ver_empleado(self, id_empleado):
        query = "SELECT * FROM empleado WHERE id_empleado = ?"
        valores = (id_empleado,)
        return Conexion.ejecutar(query, valores)

    def actualizar_empleado(self, id_empleado, nombre, direccion, telefono, email, fecha_inicio_contrato, salario):
        query = """UPDATE empleado 
                    SET nombre = ?, direccion = ?, telefono = ?, email = ?, fecha_inicio_contrato = ?, salario = ? 
                    WHERE id_empleado = ?;"""
        valores = (nombre, direccion, telefono, email, fecha_inicio_contrato, salario, id_empleado)
        Conexion.ejecutar(query, valores)

    def eliminar_empleado(self,id_empleado):
        query = "DELETE FROM empleado WHERE id_empleado = ?;"
        valores = (id_empleado,)
        Conexion.ejecutar(query, valores)
            
    def crear_departamento(self, nombre):
        query = """INSERT INTO departamento ( nombre) 
                    VALUES (?)"""
        valores = (nombre,)
        Conexion.ejecutar(query, valores)

    def ver_departamento(self, id_departamento):
        query = "SELECT * FROM departamento WHERE id_departamento = ?"
        valores = (id_departamento,)
        return Conexion.ejecutar(query, valores)

    def actualizar_departamento(self,id_departamento, nombre):
        query = """UPDATE departamento
                    SET nombre = ?
                    WHERE id_departamento = ?;"""
        valores = (nombre, id_departamento)
        Conexion.ejecutar(query, valores)

    def eliminar_departamento(self, id_departamento):
        query = "DELETE FROM departamento WHERE id_departamento = ?;"
        valores = (id_departamento,)
        Conexion.ejecutar(query, valores)

    def crear_proyecto(self, nombre, descripcion, fecha_inicio, lista_proyectos):
        query = """INSERT INTO proyecto (nombre, descripcion, fecha_inicio) 
                    VALUES (?, ?, ?)"""
        valores = (nombre, descripcion, fecha_inicio)
        Conexion.ejecutar(query, valores)

    def ver_proyecto(self, id_proyecto):
        query = "SELECT * FROM proyecto WHERE id_proyecto = ?"
        valores = (id_proyecto,)
        return Conexion.ejecutar(query, valores)

    def actualizar_proyecto(self, id_proyecto, nombre):
        query = """UPDATE proyecto
                    SET nombre = ?
                    WHERE id_proyecto = ?;"""
        valores = (nombre, id_proyecto)
        Conexion.ejecutar(query, valores) 

    def asignar_empleado_a_departamento(self, id_empleado, id_departamento):
        query = """UPDATE empleado
                    SET id_departamento = ?
                    WHERE id_empleado = ?;"""
        valores = (id_departamento, id_empleado)
        Conexion.ejecutar(query, valores)

class UsuarioComun(Usuario):
    def __init__(self, username, password):
        super().__init__(username, password)
        self.tipo_usuario = "comun"

    def registrar_horas(self, fecha, horas, descripcion, proyecto):
        query = """INSERT INTO registro_horas (fecha, horas, descripcion, proyecto) 
                    VALUES (?, ?, ?, ?)"""
        valores = (fecha, horas, descripcion, proyecto)
        Conexion.ejecutar(query, valores) 
       
class ServicioInformes:
    def generar_informe(self, item):
        query = f"SELECT * FROM {item}"
        resultado = Conexion.ejecutar(query, '')
        df = DataFrame(resultado) #solo excel
        excel_file = f"informe_{item}.xlsx"
        df.to_excel(excel_file, index=False, sheet_name=item)

'''
usuarios = ListaUsuarios()
admin = usuarios.usuarios[0]
#admin.crear_empleado("Juan Lopez", "1234", "987654321", "juan@mail.com", "18-04-2000", 100000)
print(admin.ver_empleado(2))
#admin.crear_departamento("ventas")
admin.asignar_empleado_a_departamento(2, 1)
print(admin.ver_empleado(2))
serv_informes = ServicioInformes()
#serv_informes.generar_informe("empleado", "pdf")
serv_informes.generar_informe("empleado")
'''
