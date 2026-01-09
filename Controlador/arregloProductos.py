from Controlador.productos import producto
#Mantenimiento para los productos

class ArregloProductos():

    #Atributo
    dataProducto = [] #<--Nuestra base de datos

    #Constructor (vacio)
    def __init__(self):
        self.cargar()

    def adicionaProducto(self,objpro):
        self.dataProducto.append(objpro)

    def devolverProducto(self, pos):
        return self.dataProducto[pos]

    def tamañoArregloProducto(self):
        return len(self.dataProducto)

    def buscarProducto(self, codigo):
        for i in range (self.tamañoArregloProducto()):
            if codigo == self.dataProducto[i].getCodigoProducto():
                return i
        return -1

    def eliminarProducto(self, pos):
        del(self.dataProducto[pos])

    def modificarProducto(self, objpro, pos):
        self.dataProducto[pos] = objpro

    def retornarDatos(self):
        return self.dataProducto

    def grabar(self):
        #Graba todos los datos de la lista dataProductos hacia el archivo Productos.txt
        archivo = open("Modelo/Productos.txt", "w+", encoding = "utf-8")
        for i in range(self.tamañoArregloProducto()):
            archivo.write(str(self.devolverProducto(i).getCodigoProducto()) + ","
            + str(self.devolverProducto(i).getNombreProducto()) + ","
            + str(self.devolverProducto(i).getDescripcionProducto()) + ","
            + str(self.devolverProducto(i).getStockMinimo()) + ","
            + str(self.devolverProducto(i).getStockActual()) + ","
            + str(self.devolverProducto(i).getPrecioVenta()) + ","
            + str(self.devolverProducto(i).getPrecioCosto()) + ","
            + str(self.devolverProducto(i).getProveedor()) + ","
            + str(self.devolverProducto(i).getAlmacen()) + "\n")
        archivo.close()
    
    def cargar(self):
        #Carga los datos del archivo de texto Productos.txt y los pasa a la lista dataProductos[]
        # con la finalidad de imprimir esos datos en la tabla
        archivo = open("Modelo/Productos.txt", "a+", encoding = "utf-8") #a+ para que escriba y cree el archivo txt si no existe
        archivo.seek(0) #para que lea desde el inicio
        for linea in archivo.readlines():
            columna = str(linea).split(",")
            codigo = columna[0]
            nombre = columna[1]
            descripcionproducto = columna[2]
            stockminimo = columna[3]
            stockactual = columna[4]
            preciocosto = columna[5]
            precioventa = columna[6]
            proveedor = columna[7]
            almacen = columna[8].strip()
            objPro = producto(codigo, nombre, descripcionproducto, stockminimo, stockactual, preciocosto, precioventa, proveedor, almacen)
            self.adicionaProducto(objPro)
        archivo.close()

