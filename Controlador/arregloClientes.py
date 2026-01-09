from Controlador.clientes import cliente
#Mantenimiento para los clientes

class ArregloClientes():

    #Atributo
    dataCliente = [] #<--Nuestra base de datos

    #Constructor (vacio)
    def __init__(self):
        self.cargar()

    def adicionaCliente(self,objcli):
        self.dataCliente.append(objcli)

    def devolverCliente(self, pos):
        return self.dataCliente[pos]

    def tamañoArregloCliente(self):
        return len(self.dataCliente)

    def buscarCliente(self, dni):
        for i in range (self.tamañoArregloCliente()):
            if dni == self.dataCliente[i].getDniCliente():
                return i
        return -1

    def eliminarCliente(self, pos):
        del(self.dataCliente[pos])

    def modificarCliente(self, objcli, pos):
        self.dataCliente[pos] = objcli

    def retornarDatos(self):
        return self.dataCliente

    def grabar(self):
        #Graba todos los datos de la lista dataClientes hacia el archivo Clientes.txt
        archivo = open("Modelo/Clientes.txt", "w+", encoding = "utf-8")
        for i in range(self.tamañoArregloCliente()):
            archivo.write(str(self.devolverCliente(i).getDniCliente()) + ","
            + str(self.devolverCliente(i).getNombresCliente()) + ","
            + str(self.devolverCliente(i).getApellidoPaternoCliente()) + ","
            + str(self.devolverCliente(i).getApellidoMaternoCliente()) + ","
            + str(self.devolverCliente(i).getDireccionCliente()) + ","
            + str(self.devolverCliente(i).getTelefonoCliente()) + "\n")
        archivo.close()
    
    def cargar(self):
        #Carga los datos del archivo de texto Clientes.txt y los pasa a la lista dataClientes[]
        # con la finalidad de imprimir esos datos en la tabla
        archivo = open("Modelo/Clientes.txt", "a+", encoding = "utf-8") #a+ para que escriba y cree el archivo txt si no existe
        archivo.seek(0) #para que lea desde el inicio
        for linea in archivo.readlines():
            columna = str(linea).split(",")
            dni = columna[0]
            nombres = columna[1]
            apellido_paterno = columna[2]
            apellido_materno = columna[3]
            direccion = columna[4]
            telefono = columna[5].strip()
            objCli = cliente(dni, nombres, apellido_paterno, apellido_materno, direccion, telefono)
            self.adicionaCliente(objCli)
        archivo.close()

