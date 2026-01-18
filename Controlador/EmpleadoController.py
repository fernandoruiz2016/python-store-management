from Repository.EmpleadoRepository import EmpleadoRepository
from Modelo.empleados import empleado

class EmpleadoController():

    @staticmethod
    def registrar(datos):
        if not datos:
            raise ValueError("Faltan los datos del empleado")
        
        dni, nombres, ap_pat, ap_mat, direccion, telefono = datos
        if not dni:
            raise ValueError("DNI obligatorio")
        
        emp = empleado(
            dni,
            nombres,
            ap_pat,
            ap_mat,
            direccion,
            telefono
        )
        return EmpleadoRepository.registrar(emp)

    @staticmethod
    def listar():
        try:
            return EmpleadoRepository.listar()
        except Exception:
            raise ValueError("Error al listar empleados")

    @staticmethod
    def buscar(dni):
        if not dni:
            raise ValueError("Debe ingresar un DNI")
        return EmpleadoRepository.buscar(dni)

    @staticmethod
    def modificar(datos):
        if not datos:
            raise ValueError("Faltan los datos del empleado")
        
        dni, nombres, ap_pat, ap_mat, direccion, telefono = datos
        if not dni:
            raise ValueError("DNI obligatorio")
        
        emp = empleado(
            dni,
            nombres,
            ap_pat,
            ap_mat,
            direccion,
            telefono
        )
        return EmpleadoRepository.modificar(emp)

    @staticmethod
    def eliminar(dni):
        if not dni:
            raise ValueError("Debe seleccionar un empleado")

        if not EmpleadoRepository.buscar(dni):
            raise ValueError("El empleado no existe")

        return EmpleadoRepository.eliminar(dni)
