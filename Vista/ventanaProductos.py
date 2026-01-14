#Programando el comportamiento de la ventana ventanaProductos.py
#Y su comportamiento inicial

from PyQt5 import QtWidgets ,uic
from PyQt5 import QtGui
import re

from Controlador.arregloProductos import ArregloProductos, producto
# Creamos el objteo aPro el cual podrá usar todos los métodos de arregloProductos
aPro = ArregloProductos()

# QtGui --> usiliza los botones del formulario

class VentanaProductos(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super(VentanaProductos, self).__init__(parent)
        uic.loadUi("UI/ventanaProductos.ui", self)#==> se debe colocar el nombre y ruta del formulario
        # self.show()
        self.consultado = False #<- Para la funcion Eliminar

        # Eventos
        self.tblProductos.clicked.connect(self.seleccionarFilaTabla)

        self.btnConsultar.clicked.connect(self.consultar)
        self.btnRegistrar.clicked.connect(self.registrar)
        self.btnEliminar.clicked.connect(self.eliminar)
        self.btnQuitar.clicked.connect(self.quitar)
        self.btnModificar.clicked.connect(self.modificar)
        self.btnListar.clicked.connect(self.listar)
        # self.Carga_Productos()
        self.listar()

    # Es necesario tener algunos metodos a partir de aqui
    def Carga_Productos(self):
        if aPro.tamañoArregloProducto()==0:
            objPro= producto('P0001','Leche','Evaporada', 50, 100, 1.0, 2.5, 'Gloria', 'Lacteos')
            aPro.adicionaProducto(objPro)
            objPro= producto('P0002','Fideos','Fetuccini', 30, 40, 1.1, 3.2, 'Nicolini', 'Trigos')
            aPro.adicionaProducto(objPro)
            objPro= producto('P0003','Manzana','Israel', 40, 70, 0.4, 1.5, 'Alicorp', 'Frutas')
            aPro.adicionaProducto(objPro)
            objPro= producto('P0004','Aloe','Bebida', 10, 50, 0.7, 2.5, 'AJE', 'Verduras')
            aPro.adicionaProducto(objPro)
            self.listar()
        else:
            self.listar()

    def obtenerCodigo(self):
        return self.txtCodigo.text()
    
    def obtenerNombre(self):
        return self.txtNombre.text()

    def obtenerDescripcion(self):
        return self.txtDescripcion.text()

    def obtenerStockMinimo(self):
        return self.txtStockMinimo.text()

    def obtenerStockActual(self):
        return self.txtStockActual.text()

    def obtenerPrecioCosto(self):
        return self.txtPrecioCosto.text()

    def obtenerPrecioVenta(self):
        return self.txtPrecioVenta.text()

    def obtenerProveedor(self):
        return self.cboProveedor.currentText()

    def obtenerAlmacen(self):
        return self.cboAlmacen.currentText()

    def limpiarTabla(self):
        self.tblProductos.clearContents()
        self.tblProductos.setRowCount(0)

    def valida(self):
        if self.txtCodigo.text() =="":
            self.txtCodigo.setFocus()
            return "Codigo del producto...!!!"
        if not re.match(r"^P\d{2,}$", self.txtCodigo.text()):
            self.txtCodigo.setFocus()
            return "Código inválido. Ejemplo: P01, P10, P100"
        elif self.txtNombre.text()=="":
            self.txtNombre.setFocus()
            return "Nombre del producto...!!!"
        elif self.txtDescripcion.text()=="":
            self.txtDescripcion.setFocus()
            return "Descripcion del producto...!!!"
        elif self.txtStockMinimo.text()=="":
            self.txtStockMinimo.setFocus()
            return "Stock Minimo del producto...!!!"
        elif self.txtStockActual.text()=="":
            self.txtStockActual.setFocus()
            return "Stock Actual del producto...!!!"
        elif self.txtPrecioCosto.text()=="":
            self.txtPrecioCosto.setFocus()
            return "Precio Costo del producto...!!!"
        elif self.txtPrecioVenta.text()=="":
            self.txtPrecioVenta.setFocus()
            return "Precio Venta del producto...!!!"
        elif self.cboProveedor.currentIndex()==0:
            self.cboProveedor.setFocus()
            return "Proveedor del producto...!!!"
        elif self.cboAlmacen.currentIndex()==0:
            self.cboAlmacen.setFocus()
            return "Almacen del producto...!!!"
        else:
            return ""

    def listar(self):
        self.tblProductos.setRowCount(aPro.tamañoArregloProducto())
        self.tblProductos.setColumnCount(9)
        #Cabecera
        self.tblProductos.verticalHeader().setVisible(False)
        for i in range (0, aPro.tamañoArregloProducto()):
            self.tblProductos.setItem(i, 0, QtWidgets.QTableWidgetItem(aPro.devolverProducto(i).getCodigoProducto()))
            self.tblProductos.setItem(i, 1, QtWidgets.QTableWidgetItem(aPro.devolverProducto(i).getNombreProducto()))
            self.tblProductos.setItem(i, 2, QtWidgets.QTableWidgetItem(aPro.devolverProducto(i).getDescripcionProducto()))
            self.tblProductos.setItem(i, 3, QtWidgets.QTableWidgetItem(aPro.devolverProducto(i).getStockMinimo()))
            self.tblProductos.setItem(i, 4, QtWidgets.QTableWidgetItem(aPro.devolverProducto(i).getStockActual()))
            self.tblProductos.setItem(i, 5, QtWidgets.QTableWidgetItem(aPro.devolverProducto(i).getPrecioCosto()))
            self.tblProductos.setItem(i, 6, QtWidgets.QTableWidgetItem(aPro.devolverProducto(i).getPrecioVenta()))
            self.tblProductos.setItem(i, 7, QtWidgets.QTableWidgetItem(aPro.devolverProducto(i).getProveedor()))
            self.tblProductos.setItem(i, 8, QtWidgets.QTableWidgetItem(aPro.devolverProducto(i).getAlmacen()))
        self.consultado = False

    def limpiarControles(self):
        self.txtCodigo.clear()
        self.txtNombre.clear()
        self.txtDescripcion.clear()
        self.txtStockMinimo.clear()
        self.txtStockActual.clear()
        self.txtPrecioCosto.setText("S/. ")
        self.txtPrecioVenta.setText("S/. ")
        self.cboProveedor.setCurrentIndex(0)
        self.cboAlmacen.setCurrentIndex(0)

    # Mantenimientos (Grabar (Registrar), Consultar, Modificar, Listar, Quitar)
    def registrar(self):
        if self.valida() == "":
            objPro= producto(self.obtenerCodigo(), self.obtenerNombre(),
                            self.obtenerDescripcion(),
                            self.obtenerStockMinimo(),
                            self.obtenerStockActual(),
                            self.obtenerPrecioCosto(),
                            self.obtenerPrecioVenta(),
                            self.obtenerProveedor(),
                            self.obtenerAlmacen())
            codigo=self.obtenerCodigo()
            if aPro.buscarProducto(codigo) == -1:
                aPro.adicionaProducto(objPro)
                aPro.grabar()
                self.limpiarControles()
                self.listar()
            else:
                QtWidgets.QMessageBox.information(self, "Registrar Producto",
                                                  "El Codigo ingresado ya existe... !!!",
                                                  QtWidgets.QMessageBox.Ok)
        else:
            QtWidgets.QMessageBox.information(self, "Registrar Producto",
                                                  "Error en " + self.valida(), QtWidgets.QMessageBox.Ok)

    def consultar(self):
        #self.limpiarTabla()
        if aPro.tamañoArregloProducto() == 0:
                QtWidgets.QMessageBox.information(self, "Consultar Producto",
                                                  "No existe productos a consultar... !!!",
                                                  QtWidgets.QMessageBox.Ok)
        else:
            codigo, _ = QtWidgets.QInputDialog.getText(self, "Consultar Producto",
                                                  "Ingrese el Código a consultar")
            pos = aPro.buscarProducto(codigo)
            if pos == -1:
                QtWidgets.QMessageBox.information(self, "Consultar Producto",
                                                  "El Codigo ingresado no existe... !!!",
                                                  QtWidgets.QMessageBox.Ok)
            else:
                self.txtCodigo.setText(aPro.devolverProducto(pos).getCodigoProducto())
                self.txtNombre.setText(aPro.devolverProducto(pos).getNombreProducto())
                self.txtDescripcion.setText(aPro.devolverProducto(pos).getDescripcionProducto())
                self.txtStockMinimo.setText(aPro.devolverProducto(pos).getStockMinimo())
                self.txtStockActual.setText(aPro.devolverProducto(pos).getStockActual())
                self.txtPrecioCosto.setText(aPro.devolverProducto(pos).getPrecioCosto())
                self.txtPrecioVenta.setText(aPro.devolverProducto(pos).getPrecioVenta())
                self.cboProveedor.setCurrentText(aPro.devolverProducto(pos).getProveedor())
                self.cboAlmacen.setCurrentText(aPro.devolverProducto(pos).getAlmacen())

                self.tblProductos.setRowCount(1)
                self.tblProductos.setItem(0,0, QtWidgets.QTableWidgetItem(aPro.devolverProducto(pos).getCodigoProducto()))
                self.tblProductos.setItem(0,1, QtWidgets.QTableWidgetItem(aPro.devolverProducto(pos).getNombreProducto()))
                self.tblProductos.setItem(0,2, QtWidgets.QTableWidgetItem(aPro.devolverProducto(pos).getDescripcionProducto()))
                self.tblProductos.setItem(0,3, QtWidgets.QTableWidgetItem(aPro.devolverProducto(pos).getStockMinimo()))
                self.tblProductos.setItem(0,4, QtWidgets.QTableWidgetItem(aPro.devolverProducto(pos).getStockActual()))
                self.tblProductos.setItem(0,5, QtWidgets.QTableWidgetItem(aPro.devolverProducto(pos).getPrecioCosto()))
                self.tblProductos.setItem(0,6, QtWidgets.QTableWidgetItem(aPro.devolverProducto(pos).getPrecioVenta()))
                self.tblProductos.setItem(0,7, QtWidgets.QTableWidgetItem(aPro.devolverProducto(pos).getProveedor()))
                self.tblProductos.setItem(0,8, QtWidgets.QTableWidgetItem(aPro.devolverProducto(pos).getAlmacen()))
                
                self.consultado = True

    def eliminar(self):
        if self.consultado == False:
            QtWidgets.QMessageBox.information(self, "Consulte Producto",
                                              "Por favor consultar el codigo",
                                              QtWidgets.QMessageBox.Ok)
        else:
            codigo = self.txtCodigo.text()
            pos = aPro.buscarProducto(codigo)
            aPro.eliminarProducto(pos)
            aPro.grabar()
            self.limpiarControles()
            self.listar()

    def quitar(self):
        if aPro.tamañoArregloProducto() ==0:
            QtWidgets.QMessageBox.information(self, "Eliminar Producto",
                                              "No existe productos a eliminar... !!!",
                                              QtWidgets.QMessageBox.Ok)
        else:
            fila=self.tblProductos.selectedItems()
            if fila:
                indiceFila=fila[0].row()
                codigo=self.tblProductos.item(indiceFila, 0).text()
                pos =aPro.buscarProducto(codigo)
                aPro.eliminarProducto(pos)
                aPro.grabar()
                self.limpiarTabla()
                self.listar()
            else:
                QtWidgets.QMessageBox.information(self, "Eliminar Producto",
                                                  "Debe seleccionar una fila... !!!",
                                                  QtWidgets.QMessageBox.Ok)

    def seleccionarFilaTabla(self):
        fila = self.tblProductos.currentRow()

        self.txtCodigo.setText(self.tblProductos.item(fila,0).text())
        self.txtNombre.setText(self.tblProductos.item(fila,1).text())
        self.txtDescripcion.setText(self.tblProductos.item(fila,2).text())
        self.txtStockMinimo.setText(self.tblProductos.item(fila,3).text())
        self.txtStockActual.setText(self.tblProductos.item(fila,4).text())
        self.txtPrecioCosto.setText(self.tblProductos.item(fila,5).text())
        self.txtPrecioVenta.setText(self.tblProductos.item(fila,6).text())
        self.cboProveedor.setCurrentText(self.tblProductos.item(fila,7).text())
        self.cboAlmacen.setCurrentText(self.tblProductos.item(fila,8).text())

    def modificar(self):
        if aPro.tamañoArregloProducto() == 0:
            QtWidgets.QMessageBox.information(self, "Modificar Producto",
                                                  "No existen productos a Modificar... !!!",
						                    QtWidgets.QMessageBox.Ok)
        else:
            try:
                fila=self.tblProductos.selectedItems()
                
                indiceFila=fila[0].row()
                self.txtCodigo.setText(self.tblProductos.item(indiceFila, 0).text())

                codigo= self.obtenerCodigo()
                pos= aPro.buscarProducto(codigo)
                if pos != -1:
                    if self.valida() == "":
                        objPro= producto(self.obtenerCodigo(), self.obtenerNombre(),
                                    self.obtenerDescripcion(),
                                    self.obtenerStockMinimo(),
                                    self.obtenerStockActual(),
                                    self.obtenerPrecioCosto(),
                                    self.obtenerPrecioVenta(),
                                    self.obtenerProveedor(),
                                    self.obtenerAlmacen())
                        aPro.modificarProducto(objPro, pos)
                        aPro.grabar()
                        self.limpiarControles()
                        self.listar()
                    else:
                        QtWidgets.QMessageBox.information(self, "Registrar Producto",
                                                  "Error en " + self.valida(), QtWidgets.QMessageBox.Ok)
            except:
                QtWidgets.QMessageBox.information(self, "Modificar Producto",
                                                  "Seleccione un producto a Modificar... !!!",
						                        QtWidgets.QMessageBox.Ok)


