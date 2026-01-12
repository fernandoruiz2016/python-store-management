from Controlador.comprobantes import comprobante
#Mantenimiento para los comprobantes

class ArregloComprobantes():

    #Atributo
    dataComprobante = [] #<--Nuestra base de datos

    #Constructor (vacio)
    def __init__(self):
        self.cargar()

    def adicionaComprobante(self,objcom):
        self.dataComprobante.append(objcom)

    def devolverComprobante(self, pos):
        return self.dataComprobante[pos]

    def tamañoArregloComprobante(self):
        return len(self.dataComprobante)

    def buscarComprobante(self, id):
        for i in range (self.tamañoArregloComprobante()):
            if id == self.dataComprobante[i].getIdComprobante():
                return i
        return -1

    def eliminarComprobante(self, pos):
        del(self.dataComprobante[pos])

    def modificarComprobante(self, objCom, pos):
        self.dataComprobante[pos] = objCom

    def retornarDatos(self):
        return self.dataComprobante

    def grabar(self):
        #Graba todos los datos de la lista dataComprobante hacia el archivo Comprobantes.txt
        archivo = open("Modelo/Comprobantes.txt", "w+", encoding = "utf-8")
        for i in range(self.tamañoArregloComprobante()):
            archivo.write(str(self.devolverComprobante(i).getIdComprobante()) + ","
            + str(self.devolverComprobante(i).getTipo()) + ","
            + str(self.devolverComprobante(i).getFecha()) + ","
            + str(self.devolverComprobante(i).getTotal()) + "\n")
        archivo.close()
    
    def cargar(self):
        #Carga los datos del archivo de texto Comprobantes.txt y los pasa a la lista dataComprobante[]
        # con la finalidad de imprimir esos datos en la tabla
        archivo = open("Modelo/Comprobantes.txt", "a+", encoding = "utf-8") #a+ para que escriba y cree el archivo txt si no existe
        archivo.seek(0) #para que lea desde el inicio
        for linea in archivo.readlines():
            columna = str(linea).split(",")
            id = columna[0]
            tipo = columna[1]
            fecha = columna[2]
            total = columna[3].strip()
            objCom = comprobante(id, tipo, fecha, total)
            self.adicionaComprobante(objCom)
        archivo.close()

