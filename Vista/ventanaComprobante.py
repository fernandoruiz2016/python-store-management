#Programando el comportamiento de la ventana ventanaClientes.py
#Y su comportamiento inicial

from PyQt5 import QtWidgets ,uic
from PyQt5 import QtGui

from Controlador.arregloComprobantes import ArregloComprobantes, comprobante
# Creamos el objteo aCom el cual podrá usar todos los métodos de arregloClientes
aCom = ArregloComprobantes()

# QtGui --> usiliza los botones del formulario

class VentanaClientes(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super(VentanaClientes, self).__init__(parent)
        uic.loadUi("UI/ventanaComprobantes.ui", self)#==> se debe colocar el nombre y ruta del formulario
        # self.show()
        self.consultado = False #<- Para la funcion Eliminar

        # Eventos
        self.tblComprobantes.clicked.connect(self.seleccionarFilaTabla)

        self.btnConsultar.clicked.connect(self.consultar)
        self.btnRegistrar.clicked.connect(self.registrar)
        self.btnEliminar.clicked.connect(self.eliminar)
        self.btnQuitar.clicked.connect(self.quitar)
        self.btnModificar.clicked.connect(self.modificar)
        self.btnListar.clicked.connect(self.listar)
        # self.Carga_Comprobantes()
        self.listar()

    # Es necesario tener algunos metodos a partir de aqui
    def Carga_Comprobantes(self):
        if aCom.tamañoArregloComprobante()==0:
            aCom= comprobante('F001','Factura','2026-01-03', 55)
            aCom.adicionaComprobante(aCom)
            aCom= comprobante('B001','Boleta','2026-01-04', 20)
            self.listar()
        else:
            self.listar()

    def obtenerId(self):
        return self.txtId.text()
    
    def obtenerTipo(self):
        return self.txtTipo.text()

    def obtenerFecha(self):
        return self.dtFecha.date().toPyDate()

    def obtenerTotal(self):
        return self.txtTotal.text()

    def limpiarTabla(self):
        self.tblComprobantes.clearContents()
        self.tblComprobantes.setRowCount(0)

    def valida(self):
        if self.txtId.text() =="":
            self.txtId.setFocus()
            return "Id del comprobante...!!!"
        elif self.txtTipo.text()=="":
            self.txtTipo.setFocus()
            return "Tipo del comprobante...!!!"
        elif self.dtFecha.text()=="":
            self.dtFecha.setFocus()
            return "Fecha del comprobante...!!!"
        elif self.txtTotal.text()=="":
            self.txtTotal.setFocus()
            return "Importe total del comprobante...!!!"
        else:
            return ""

    def listar(self):
        self.tblComprobantes.setRowCount(aCom.tamañoArregloComprobante())
        self.tblComprobantes.setColumnCount(6)
        #Cabecera
        self.tblComprobantes.verticalHeader().setVisible(False)
        for i in range (0, aCom.tamañoArregloComprobante()):
            self.tblComprobantes.setItem(i, 0, QtWidgets.QTableWidgetItem(aCom.devolverCliente(i).getIdComprobante()))
            self.tblComprobantes.setItem(i, 1, QtWidgets.QTableWidgetItem(aCom.devolverCliente(i).getTipo()))
            self.tblComprobantes.setItem(i, 2, QtWidgets.QTableWidgetItem(aCom.devolverCliente(i).getFecha()))
            self.tblComprobantes.setItem(i, 3, QtWidgets.QTableWidgetItem(aCom.devolverCliente(i).getTotal()))
        self.consultado = False

    def limpiarControles(self):
        self.txtId.clear()
        self.txtTipo.clear()
        self.dtFecha.clear()
        self.txtTotal.clear()
        self.txtDireccion.clear()
        self.txtTelefono.clear()

    # Mantenimientos (Grabar (Registrar), Consultar, Modificar, Listar, Quitar)
    def registrar(self):
        if self.valida() == "":
            aCom= comprobante(self.obtenerId(), self.obtenerTipo(),
                            self.obtenerFecha(),
                            self.obtenerTotal())
            id=self.obtenerId()
            if aCom.buscarComprobante(id) == -1:
                aCom.adicionaComprobante(aCom)
                aCom.grabar()
                self.limpiarControles()
                self.listar()
            else:
                QtWidgets.QMessageBox.information(self, "Registrar Comprobante",
                                                  "El id ingresado ya existe... !!!",
                                                  QtWidgets.QMessageBox.Ok)
        else:
            QtWidgets.QMessageBox.information(self, "Registrar Comprobante",
                                                  "Error en " + self.valida(), QtWidgets.QMessageBox.Ok)

    def consultar(self):
        #self.limpiarTabla()
        if aCom.tamañoArregloComprobante() == 0:
                QtWidgets.QMessageBox.information(self, "Consultar Comprobante",
                                                  "No existe comprobantes a consultar... !!!",
                                                  QtWidgets.QMessageBox.Ok)
        else:
            id, _ = QtWidgets.QInputDialog.getText(self, "Consultar Comprobante",
                                                  "Ingrese el id a consultar")
            pos = aCom.buscarComprobante(id)
            if pos == -1:
                QtWidgets.QMessageBox.information(self, "Consultar Comprobante",
                                                  "El Id ingresado no existe... !!!",
                                                  QtWidgets.QMessageBox.Ok)
            else:
                self.txtId.setText(aCom.devolverCliente(pos).getIdComprobante())
                self.txtTipo.setText(aCom.devolverCliente(pos).getTipo())
                self.dtFecha.setText(aCom.devolverCliente(pos).getFecha())
                self.txtTotal.setText(aCom.devolverCliente(pos).getTotal())

                self.tblComprobantes.setRowCount(1)
                self.tblComprobantes.setItem(0,0, QtWidgets.QTableWidgetItem(aCom.devolverCliente(pos).getIdComprobante()))
                self.tblComprobantes.setItem(0,1, QtWidgets.QTableWidgetItem(aCom.devolverCliente(pos).getTipo()))
                self.tblComprobantes.setItem(0,2, QtWidgets.QTableWidgetItem(aCom.devolverCliente(pos).getFecha()))
                self.tblComprobantes.setItem(0,3, QtWidgets.QTableWidgetItem(aCom.devolverCliente(pos).getTotal()))

                self.consultado = True

    def eliminar(self):
        if self.consultado == False:
            QtWidgets.QMessageBox.information(self, "Consulte Comprobante",
                                              "Por favor consultar el Id",
                                              QtWidgets.QMessageBox.Ok)
        else:
            id = self.txtId.text()
            pos = aCom.buscarComprobante(id)
            aCom.eliminarComprobante(pos)
            aCom.grabar()
            self.limpiarControles()
            self.listar()

    def quitar(self):
        if aCom.tamañoArregloComprobante() ==0:
            QtWidgets.QMessageBox.information(self, "Eliminar Comprobante",
                                              "No existe comprobantes a eliminar... !!!",
                                              QtWidgets.QMessageBox.Ok)
        else:
            fila=self.tblComprobantes.selectedItems()
            if fila:
                indiceFila=fila[0].row()
                id=self.tblComprobantes.item(indiceFila, 0).text()
                pos =aCom.buscarComprobante(id)
                aCom.eliminarComprobante(pos)
                aCom.grabar()
                self.limpiarTabla()
                self.listar()
            else:
                QtWidgets.QMessageBox.information(self, "Eliminar Comprobante",
                                                  "Debe seleccionar una fila... !!!",
                                                  QtWidgets.QMessageBox.Ok)

    def seleccionarFilaTabla(self):
        fila = self.tblComprobantes.currentRow()

        self.txtId.setText(self.tblComprobantes.item(fila,0).text())
        self.txtTipo.setText(self.tblComprobantes.item(fila,1).text())
        self.dtFecha.setText(self.tblComprobantes.item(fila,2).text())
        self.txtTotal.setText(self.tblComprobantes.item(fila,3).text())
        self.txtDireccion.setText(self.tblComprobantes.item(fila,4).text())
        self.txtTelefono.setText(self.tblComprobantes.item(fila,5).text())

    def modificar(self):
        if aCom.tamañoArregloComprobante() == 0:
            QtWidgets.QMessageBox.information(self, "Modificar Comprobante",
                                                  "No existen comprobantes a Modificar... !!!",
						   QtWidgets.QMessageBox.Ok)
        else:
            try:
                fila=self.tblComprobantes.selectedItems()
                
                indiceFila=fila[0].row()
                self.txtId.setText(self.tblComprobantes.item(indiceFila, 0).text())

                id= self.obtenerId()
                pos= aCom.buscarComprobante(id)
                if pos != -1:
                    if self.valida() == "":
                        aCom= comprobante(self.obtenerId(), self.obtenerTipo(),
                                        self.obtenerFecha(),
                                        self.obtenerTotal())
                        aCom.modificarComprobante(aCom, pos)
                        aCom.grabar()
                        self.limpiarControles()
                        self.listar()
                    else:
                        QtWidgets.QMessageBox.information(self, "Modificar Comprobante",
                                                  "Error en " + self.valida(), QtWidgets.QMessageBox.Ok)
            except:
                QtWidgets.QMessageBox.information(self, "Modificar Comprobante",
                                                  "Seleccione un comprobante a Modificar... !!!",
						                        QtWidgets.QMessageBox.Ok)



