import serial as connector #para conectar con Arduino
import sys
import PyQt5
from PyQt5 import uic, QtWidgets

qtCreatorFile = "Practica1_U1.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = PyQt5.uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.btn_connect.clicked.connect(self.conectar)
        self.txt_com.textChanged.connect(self.isCOM)
        self.txt_word.textChanged.connect(self.isEmpty)
        self.btn_init.clicked.connect(self.getAscii)
        self.arduino = None #null en java


    # Área de los Slots
    def conectar(self):
        if self.arduino == None:
            com = "COM"+ self.txt_com.text()
        #    self.txt_com.setEnabled(False)
            self.arduino =  connector.Serial(com, baudrate=9600, timeout=1)  #Establece la conexion por primera vez
            print("Conexión Inicializada")
            self.lb_error.setText("");
            self.btn_connect.setText("DESCONECTAR")
        elif self.arduino.isOpen(): ##otra opción: checar que el texto del boton sea desconectar
            self.btn_connect.setText("RECONECTAR")
            self.arduino.close()
            print("Conexion Cerrada")
        else:
            self.btn_connect.setText("DESCONECTAR")
            self.arduino.open()
            self.lb_error.setText("");
            print("Conexion Reconectada")



    def isCOM(self):
        self.btn_connect.setEnabled(True)
        if not self.txt_com.text().isnumeric():
            self.btn_connect.setEnabled(False)

    def isEmpty(self):
        self.btn_init.setEnabled(True)
        if not self.txt_word.text().strip():
            self.btn_init.setEnabled(False)

    def getAscii(self):
        charArray = []
        if self.arduino != None:
            if self.arduino.isOpen():
                if not self.txt_word.text().isnumeric():
                    charArray = [ ord(w) for w in self.txt_word.text().strip()]
                    a = str(charArray)
                    a = a[1: len(a) - 1]
                    self.arduino.write(a.encode())
            else:
                self.lb_error.setText("La conexion con arduino esta cerrada");
        else:
            self.lb_error.setText("No se ha establecido conexion con arduino");


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
