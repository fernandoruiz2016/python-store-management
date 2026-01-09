from Controlador.empleados import empleado
#Mantenimiento para los empleados

class ArregloEmpleados():

    #Atributo
    dataEmpleado = [] #<--Nuestra base de datos

    #Constructor (vacio)
    def __init__(self):
        self.cargar()

    def adicionaEmpleado(self,objcli):
        self.dataEmpleado.append(objcli)

    def devolverEmpleado(self, pos):
        return self.dataEmpleado[pos]

    def tamañoArregloEmpleado(self):
        return len(self.dataEmpleado)

    def buscarEmpleado(self, dni):
        for i in range (self.tamañoArregloEmpleado()):
            if dni == self.dataEmpleado[i].getDniEmpleado():
                return i
        return -1

    def eliminarEmpleado(self, pos):
        del(self.dataEmpleado[pos])

    def modificarEmpleado(self, objcli, pos):
        self.dataEmpleado[pos] = objcli

    def retornarDatos(self):
        return self.dataEmpleado

    def grabar(self):
        #Graba todos los datos de la lista dataEmpleados hacia el archivo Empleados.txt
        archivo = open("Modelo/Empleados.txt", "w+", encoding = "utf-8")
        for i in range(self.tamañoArregloEmpleado()):
            archivo.write(str(self.devolverEmpleado(i).getDniEmpleado()) + ","
            + str(self.devolverEmpleado(i).getNombresEmpleado()) + ","
            + str(self.devolverEmpleado(i).getApellidoPaternoEmpleado()) + ","
            + str(self.devolverEmpleado(i).getApellidoMaternoEmpleado()) + ","
            + str(self.devolverEmpleado(i).getDireccionEmpleado()) + ","
            + str(self.devolverEmpleado(i).getTelefonoEmpleado()) + "\n")
        archivo.close()
    
    def cargar(self):
        #Carga los datos del archivo de texto Empleados.txt y los pasa a la lista dataEmpleados[]
        # con la finalidad de imprimir esos datos en la tabla
        archivo = open("Modelo/Empleados.txt", "a+", encoding = "utf-8") #a+ para que escriba y cree el archivo txt si no existe
        archivo.seek(0) #para que lea desde el inicio
        for linea in archivo.readlines():
            columna = str(linea).split(",")
            dni = columna[0]
            nombres = columna[1]
            apellido_paterno = columna[2]
            apellido_materno = columna[3]
            direccion = columna[4]
            telefono = columna[5].strip()
            objCli = empleado(dni, nombres, apellido_paterno, apellido_materno, direccion, telefono)
            self.adicionaEmpleado(objCli)
        archivo.close()

