import sys
from PyQt5 import QtWidgets
from Vista.login import Login
from database.crearTablas import crearTablas

if __name__=='__main__':
    crearTablas()
    app=QtWidgets.QApplication(sys.argv)
    Window = Login()
    app.exec()