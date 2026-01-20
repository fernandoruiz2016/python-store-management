#Programando el comportamiento de la ventana ventanaEmpleados.py
#Y su comportamiento inicial

from PyQt5 import QtWidgets ,uic
from PyQt5 import QtGui

from Controlador.empleadoController import EmpleadoController

# QtGui --> utiliza los botones del formulario

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
        elif not self.txtDni.text().isdigit():
            self.txtDni.setFocus()
            return "DNI debe contener solo números"
        elif len(self.txtDni.text()) != 8:
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
        try:
            empleados = EmpleadoController.listar()
            
            self.tblEmpleados.setRowCount(len(empleados))
            self.tblEmpleados.setColumnCount(6)
            #Cabecera
            self.tblEmpleados.verticalHeader().setVisible(False)
            for i,emp in enumerate(empleados):
                self.tblEmpleados.setItem(i, 0, QtWidgets.QTableWidgetItem(emp.getDniEmpleado()))
                self.tblEmpleados.setItem(i, 1, QtWidgets.QTableWidgetItem(emp.getNombresEmpleado()))
                self.tblEmpleados.setItem(i, 2, QtWidgets.QTableWidgetItem(emp.getApellidoPaternoEmpleado()))
                self.tblEmpleados.setItem(i, 3, QtWidgets.QTableWidgetItem(emp.getApellidoMaternoEmpleado()))
                self.tblEmpleados.setItem(i, 4, QtWidgets.QTableWidgetItem(emp.getDireccionEmpleado()))
                self.tblEmpleados.setItem(i, 5, QtWidgets.QTableWidgetItem(emp.getTelefonoEmpleado()))
            self.consultado = False
        except ValueError as e:
            QtWidgets.QMessageBox.warning(self, "Error", str(e))

    def limpiarControles(self):
        self.txtDni.clear()
        self.txtNombres.clear()
        self.txtApellidoPaterno.clear()
        self.txtApellidoMaterno.clear()
        self.txtDireccion.clear()
        self.txtTelefono.clear()

    # Mantenimientos (Grabar (Registrar), Consultar, Modificar, Listar, Quitar)
    def registrar(self):
        try:
            if self.valida() == "":
                dni=self.obtenerDni()
                if not EmpleadoController.buscar(dni):
                    EmpleadoController.registrar((self.obtenerDni(), self.obtenerNombres(),
                                self.obtenerApellidoPaterno(), self.obtenerApellidoMaterno(),
                                self.obtenerDireccion(), self.obtenerTelefono()))
                    self.limpiarControles()
                    self.listar()
                else:
                    QtWidgets.QMessageBox.information(self, "Registrar Empleado",
                                                    "El DNI ingresado ya existe... !!!",
                                                    QtWidgets.QMessageBox.Ok)
            else:
                QtWidgets.QMessageBox.information(self, "Registrar Empleado",
                                                    "Error en " + self.valida(), QtWidgets.QMessageBox.Ok)
        
        except ValueError as e:
            QtWidgets.QMessageBox.warning(self, "Error", str(e))

    def consultar(self):
        try:
            #self.limpiarTabla()
            if len(EmpleadoController.listar()) == 0:
                    QtWidgets.QMessageBox.information(self, "Consultar Empleado",
                                                    "No existe empleados a consultar... !!!",
                                                    QtWidgets.QMessageBox.Ok)
            else:
                dni, _ = QtWidgets.QInputDialog.getText(self, "Consultar Empleado",
                                                    "Ingrese el DNI a consultar")
                emp = EmpleadoController.buscar(dni)
                if not emp:
                    QtWidgets.QMessageBox.information(self, "Consultar Empleado",
                                                    "El DNI ingresado no existe... !!!",
                                                    QtWidgets.QMessageBox.Ok)
                else:
                    self.txtDni.setText(emp[0].getDniEmpleado())
                    self.txtNombres.setText(emp[0].getNombresEmpleado())
                    self.txtApellidoPaterno.setText(emp[0].getApellidoPaternoEmpleado())
                    self.txtApellidoMaterno.setText(emp[0].getApellidoMaternoEmpleado())
                    self.txtDireccion.setText(emp[0].getDireccionEmpleado())
                    self.txtTelefono.setText(emp[0].getTelefonoEmpleado())

                    self.tblEmpleados.setRowCount(1)
                    self.tblEmpleados.setItem(0,0, QtWidgets.QTableWidgetItem(emp[0].getDniEmpleado()))
                    self.tblEmpleados.setItem(0,1, QtWidgets.QTableWidgetItem(emp[0].getNombresEmpleado()))
                    self.tblEmpleados.setItem(0,2, QtWidgets.QTableWidgetItem(emp[0].getApellidoPaternoEmpleado()))
                    self.tblEmpleados.setItem(0,3, QtWidgets.QTableWidgetItem(emp[0].getApellidoMaternoEmpleado()))
                    self.tblEmpleados.setItem(0,4, QtWidgets.QTableWidgetItem(emp[0].getDireccionEmpleado()))
                    self.tblEmpleados.setItem(0,5, QtWidgets.QTableWidgetItem(emp[0].getTelefonoEmpleado()))

                    self.consultado = True
        except ValueError as e:
            QtWidgets.QMessageBox.warning(self, "Error", str(e))

    def eliminar(self):
        try:
            if self.consultado == False:
                QtWidgets.QMessageBox.information(self, "Consulte Empleado",
                                                "Por favor consultar el dni",
                                                QtWidgets.QMessageBox.Ok)
            else:
                dni = self.txtDni.text()
                EmpleadoController.eliminar(dni)
                self.limpiarControles()
                self.listar()
        except ValueError as e:
            QtWidgets.QMessageBox.warning(self, "Error", str(e))

    def quitar(self):
        try:
            if len(EmpleadoController.listar()) ==0:
                QtWidgets.QMessageBox.information(self, "Eliminar Empleado",
                                                "No existe empleados a eliminar... !!!",
                                                QtWidgets.QMessageBox.Ok)
            else:
                fila=self.tblEmpleados.selectedItems()
                if fila:
                    indiceFila=fila[0].row()
                    dni=self.tblEmpleados.item(indiceFila, 0).text()
                    EmpleadoController.eliminar(dni)
                    self.limpiarTabla()
                    self.listar()
                else:
                    QtWidgets.QMessageBox.information(self, "Eliminar Empleado",
                                                    "Debe seleccionar una fila... !!!",
                                                    QtWidgets.QMessageBox.Ok)
        except ValueError as e:
            QtWidgets.QMessageBox.warning(self, "Error", str(e))

    def seleccionarFilaTabla(self):
        fila = self.tblEmpleados.currentRow()

        self.txtDni.setText(self.tblEmpleados.item(fila,0).text())
        self.txtNombres.setText(self.tblEmpleados.item(fila,1).text())
        self.txtApellidoPaterno.setText(self.tblEmpleados.item(fila,2).text())
        self.txtApellidoMaterno.setText(self.tblEmpleados.item(fila,3).text())
        self.txtDireccion.setText(self.tblEmpleados.item(fila,4).text())
        self.txtTelefono.setText(self.tblEmpleados.item(fila,5).text())

    def modificar(self):
        if len(EmpleadoController.listar()) == 0:
            QtWidgets.QMessageBox.information(self, "Modificar Empleado",
                                                  "No existen empleados a Modificar... !!!",
						   QtWidgets.QMessageBox.Ok)
        else:
            try:
                fila=self.tblEmpleados.selectedItems()
                
                indiceFila=fila[0].row()
                self.txtDni.setText(self.tblEmpleados.item(indiceFila, 0).text())

                dni= self.obtenerDni()
                emp= EmpleadoController.buscar(dni)
                if emp:
                    if self.valida() == "":
                        EmpleadoController.modificar((self.obtenerDni(), self.obtenerNombres(),
                                        self.obtenerApellidoPaterno(),
                                        self.obtenerApellidoMaterno(),
                                        self.obtenerDireccion(),self.obtenerTelefono()))
                        self.limpiarControles()
                        self.listar()
                    else:
                        QtWidgets.QMessageBox.information(self, "Registrar Producto",
                                                  "Error en " + self.valida(), QtWidgets.QMessageBox.Ok)
            except ValueError as e:
                QtWidgets.QMessageBox.warning(self, "Error", str(e))



