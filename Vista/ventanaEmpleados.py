#Programando el comportamiento de la ventana ventanaEmpleados.py
#Y su comportamiento inicial

from PyQt5 import QtWidgets ,uic
from PyQt5 import QtGui

from Controlador.arregloEmpleados import ArregloEmpleados, empleado
# Creamos el objteo aCli el cual podrá usar todos los métodos de arregloEmpleados
aCli = ArregloEmpleados()

# QtGui --> usiliza los botones del formulario

class VentanaEmpleados(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super(VentanaEmpleados, self).__init__(parent)
        uic.loadUi("UI/ventanaEmpleados.ui", self)#==> se debe colocar el nombre y ruta del formulario
        # self.show()
        self.consultado = False #<- Para la funcion Eliminar

        # Eventos
        self.tblEmpleados.clicked.connect(self.seleccionarFilaTabla)

        self.btnConsultar.clicked.connect(self.consultar)
        self.btnRegistrar.clicked.connect(self.registrar)
        self.btnEliminar.clicked.connect(self.eliminar)
        self.btnQuitar.clicked.connect(self.quitar)
        self.btnModificar.clicked.connect(self.modificar)
        self.btnListar.clicked.connect(self.listar)
        # self.Carga_Empleados()
        self.listar()

    # Es necesario tener algunos metodos a partir de aqui
    def Carga_Empleados(self):
        if aCli.tamañoArregloEmpleado()==0:
            objCli= empleado('08693923','Alberto','Cordero','Zamorano','Jr. Quezada 221','4585985')
            aCli.adicionaEmpleado(objCli)
            objCli= empleado('08693923','Juan','Perez','Sanchez','Jr. Cuzco 123','3722754')
            aCli.adicionaEmpleado(objCli)
            objCli= empleado('08693923','Cesar','Cespedes','Ramos','Av. Peru 162','2752854')
            aCli.adicionaEmpleado(objCli)
            objCli= empleado('08693923','Roberto','Chambi','Rojas','Jr. Cuzco 222','5714764')
            aCli.adicionaEmpleado(objCli)
            self.listar()
        else:
            self.listar()

    def obtenerDni(self):
        return self.txtDni.text()
    
    def obtenerNombres(self):
        return self.txtNombres.text()

    def obtenerApellidoPaterno(self):
        return self.txtApellidoPaterno.text()

    def obtenerApellidoMaterno(self):
        return self.txtApellidoMaterno.text()

    def obtenerDireccion(self):
        return self.txtDireccion.text()

    def obtenerTelefono(self):
        return self.txtTelefono.text()

    def limpiarTabla(self):
        self.tblEmpleados.clearContents()
        self.tblEmpleados.setRowCount(0)

    def valida(self):
        if self.txtDni.text() =="":
            self.txtDni.setFocus()
            return "DNI del empleado...!!!"
        if not self.txtDni.text().isdigit():
            self.txtDni.setFocus()
            return "DNI debe contener solo números"
        if len(self.txtDni.text()) != 8:
            self.txtDni.setFocus()
            return "DNI debe tener 8 dígitos"
        elif self.txtNombres.text()=="":
            self.txtNombres.setFocus()
            return "Nombre del empleado...!!!"
        elif self.txtApellidoPaterno.text()=="":
            self.txtApellidoPaterno.setFocus()
            return "Apellido Paterno del empleado...!!!"
        elif self.txtApellidoMaterno.text()=="":
            self.txtApellidoMaterno.setFocus()
            return "Apellido Mateno del empleado...!!!"
        elif self.txtDireccion.text()=="":
            self.txtDireccion.setFocus()
            return "Direccion del empleado...!!!"
        elif self.txtTelefono.text()=="":
            self.txtTelefono.setFocus()
            return "Telefono del empleado...!!!"
        else:
            return ""

    def listar(self):
        self.tblEmpleados.setRowCount(aCli.tamañoArregloEmpleado())
        self.tblEmpleados.setColumnCount(6)
        #Cabecera
        self.tblEmpleados.verticalHeader().setVisible(False)
        for i in range (0, aCli.tamañoArregloEmpleado()):
            self.tblEmpleados.setItem(i, 0, QtWidgets.QTableWidgetItem(aCli.devolverEmpleado(i).getDniEmpleado()))
            self.tblEmpleados.setItem(i, 1, QtWidgets.QTableWidgetItem(aCli.devolverEmpleado(i).getNombresEmpleado()))
            self.tblEmpleados.setItem(i, 2, QtWidgets.QTableWidgetItem(aCli.devolverEmpleado(i).getApellidoPaternoEmpleado()))
            self.tblEmpleados.setItem(i, 3, QtWidgets.QTableWidgetItem(aCli.devolverEmpleado(i).getApellidoMaternoEmpleado()))
            self.tblEmpleados.setItem(i, 4, QtWidgets.QTableWidgetItem(aCli.devolverEmpleado(i).getDireccionEmpleado()))
            self.tblEmpleados.setItem(i, 5, QtWidgets.QTableWidgetItem(aCli.devolverEmpleado(i).getTelefonoEmpleado()))
        self.consultado = False

    def limpiarControles(self):
        self.txtDni.clear()
        self.txtNombres.clear()
        self.txtApellidoPaterno.clear()
        self.txtApellidoMaterno.clear()
        self.txtDireccion.clear()
        self.txtTelefono.clear()

    # Mantenimientos (Grabar (Registrar), Consultar, Modificar, Listar, Quitar)
    def registrar(self):
        if self.valida() == "":
            objCli= empleado(self.obtenerDni(), self.obtenerNombres(),
                            self.obtenerApellidoPaterno(),
                            self.obtenerApellidoMaterno(),
                            self.obtenerDireccion(),
                            self.obtenerTelefono())
            dni=self.obtenerDni()
            if aCli.buscarEmpleado(dni) == -1:
                aCli.adicionaEmpleado(objCli)
                aCli.grabar()
                self.limpiarControles()
                self.listar()
            else:
                QtWidgets.QMessageBox.information(self, "Registrar Empleado",
                                                  "El DNI ingresado ya existe... !!!",
                                                  QtWidgets.QMessageBox.Ok)
        else:
            QtWidgets.QMessageBox.information(self, "Registrar Empleado",
                                                  "Error en " + self.valida(), QtWidgets.QMessageBox.Ok)

    def consultar(self):
        #self.limpiarTabla()
        if aCli.tamañoArregloEmpleado() == 0:
                QtWidgets.QMessageBox.information(self, "Consultar Empleado",
                                                  "No existe empleados a consultar... !!!",
                                                  QtWidgets.QMessageBox.Ok)
        else:
            dni, _ = QtWidgets.QInputDialog.getText(self, "Consultar Empleado",
                                                  "Ingrese el DNI a consultar")
            pos = aCli.buscarEmpleado(dni)
            if pos == -1:
                QtWidgets.QMessageBox.information(self, "Consultar Empleado",
                                                  "El DNI ingresado no existe... !!!",
                                                  QtWidgets.QMessageBox.Ok)
            else:
                self.txtDni.setText(aCli.devolverEmpleado(pos).getDniEmpleado())
                self.txtNombres.setText(aCli.devolverEmpleado(pos).getNombresEmpleado())
                self.txtApellidoPaterno.setText(aCli.devolverEmpleado(pos).getApellidoPaternoEmpleado())
                self.txtApellidoMaterno.setText(aCli.devolverEmpleado(pos).getApellidoMaternoEmpleado())
                self.txtDireccion.setText(aCli.devolverEmpleado(pos).getDireccionEmpleado())
                self.txtTelefono.setText(aCli.devolverEmpleado(pos).getTelefonoEmpleado())

                self.tblEmpleados.setRowCount(1)
                self.tblEmpleados.setItem(0,0, QtWidgets.QTableWidgetItem(aCli.devolverEmpleado(pos).getDniEmpleado()))
                self.tblEmpleados.setItem(0,1, QtWidgets.QTableWidgetItem(aCli.devolverEmpleado(pos).getNombresEmpleado()))
                self.tblEmpleados.setItem(0,2, QtWidgets.QTableWidgetItem(aCli.devolverEmpleado(pos).getApellidoPaternoEmpleado()))
                self.tblEmpleados.setItem(0,3, QtWidgets.QTableWidgetItem(aCli.devolverEmpleado(pos).getApellidoMaternoEmpleado()))
                self.tblEmpleados.setItem(0,4, QtWidgets.QTableWidgetItem(aCli.devolverEmpleado(pos).getDireccionEmpleado()))
                self.tblEmpleados.setItem(0,5, QtWidgets.QTableWidgetItem(aCli.devolverEmpleado(pos).getTelefonoEmpleado()))

                self.consultado = True

    def eliminar(self):
        if self.consultado == False:
            QtWidgets.QMessageBox.information(self, "Consulte Empleado",
                                              "Por favor consultar el dni",
                                              QtWidgets.QMessageBox.Ok)
        else:
            dni = self.txtDni.text()
            pos = aCli.buscarEmpleado(dni)
            aCli.eliminarEmpleado(pos)
            aCli.grabar()
            self.limpiarControles()
            self.listar()

    def quitar(self):
        if aCli.tamañoArregloEmpleado() ==0:
            QtWidgets.QMessageBox.information(self, "Eliminar Empleado",
                                              "No existe empleados a eliminar... !!!",
                                              QtWidgets.QMessageBox.Ok)
        else:
            fila=self.tblEmpleados.selectedItems()
            if fila:
                indiceFila=fila[0].row()
                dni=self.tblEmpleados.item(indiceFila, 0).text()
                pos =aCli.buscarEmpleado(dni)
                aCli.eliminarEmpleado(pos)
                aCli.grabar()
                self.limpiarTabla()
                self.listar()
            else:
                QtWidgets.QMessageBox.information(self, "Eliminar Empleado",
                                                  "Debe seleccionar una fila... !!!",
                                                  QtWidgets.QMessageBox.Ok)

    def seleccionarFilaTabla(self):
        fila = self.tblEmpleados.currentRow()

        self.txtDni.setText(self.tblEmpleados.item(fila,0).text())
        self.txtNombres.setText(self.tblEmpleados.item(fila,1).text())
        self.txtApellidoPaterno.setText(self.tblEmpleados.item(fila,2).text())
        self.txtApellidoMaterno.setText(self.tblEmpleados.item(fila,3).text())
        self.txtDireccion.setText(self.tblEmpleados.item(fila,4).text())
        self.txtTelefono.setText(self.tblEmpleados.item(fila,5).text())

    def modificar(self):
        if aCli.tamañoArregloEmpleado() == 0:
            QtWidgets.QMessageBox.information(self, "Modificar Empleado",
                                                  "No existen empleados a Modificar... !!!",
						   QtWidgets.QMessageBox.Ok)
        else:
            try:
                fila=self.tblEmpleados.selectedItems()
                
                indiceFila=fila[0].row()
                self.txtDni.setText(self.tblEmpleados.item(indiceFila, 0).text())

                dni= self.obtenerDni()
                pos= aCli.buscarEmpleado(dni)
                if pos != -1:
                    if self.valida() == "":
                        objCli= empleado(self.obtenerDni(), self.obtenerNombres(),
                                        self.obtenerApellidoPaterno(),
                                        self.obtenerApellidoMaterno(),
                                        self.obtenerDireccion(),self.obtenerTelefono())
                        aCli.modificarEmpleado(objCli, pos)
                        aCli.grabar()
                        self.limpiarControles()
                        self.listar()
                    else:
                        QtWidgets.QMessageBox.information(self, "Registrar Producto",
                                                  "Error en " + self.valida(), QtWidgets.QMessageBox.Ok)
            except:
                QtWidgets.QMessageBox.information(self, "Modificar Producto",
                                                  "Seleccione un producto a Modificar... !!!",
						                        QtWidgets.QMessageBox.Ok)


