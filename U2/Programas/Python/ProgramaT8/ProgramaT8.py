import serial as connector #para conectar con Arduino
import sys
import PyQt5
from PyQt5 import uic, QtWidgets
from PyQt5.QtGui import QIntValidator

qtCreatorFile = "ProgramaT8.ui"  # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = PyQt5.uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals y Configuraciones Iniciales
        self.btn_connect.clicked.connect(self.conectar)
        self.txt_com.textChanged.connect(self.isCOM)
        self.txt_com.setValidator(QIntValidator())

        self.txt_obj.setValidator(QIntValidator())
        self.txt_obj.textChanged.connect(self.isEmpty)

        self.btn_start.clicked.connect(self.start)
        self.btn_stop.clicked.connect(self.stop)

        self.arduino = None #null en java


    def conectar(self):
        if self.arduino == None:
            try:
                com = "COM" + self.txt_com.text()
                #    self.txt_com.setEnabled(False)
                self.arduino = connector.Serial(com, baudrate=9600, timeout=1)  # Establece la conexion por primera vez
                print("Conexión Inicializada")
                self.lb_error.setText("");
                self.btn_connect.setText("DESCONECTAR")
                self.lb_error.setText("")
            except Exception as e:
                print(e)
                self.lb_error.setText("COM no aceptado")
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
            self.lb_error.setText("")

    def isEmpty(self):
        self.btn_start.setEnabled(True)
        self.lb_error.setText("")
        if not self.txt_obj.text().strip():
            self.btn_start.setEnabled(False)

    def start(self):
        num = self.txt_obj.text().strip();
        if self.arduino != None:
            if self.arduino.isOpen():
                if "+" != num != "-":
                    numObj = int(num)
                    if numObj >= 0 and numObj <= 255:
                        self.arduino.write("{0}".format(numObj).encode())
                        self.btn_connect.setEnabled(False)
                        self.btn_start.setEnabled(False)
                    else:
                        self.lb_error.setText("Numero fuera del rango[0 - 255]")
                else:
                    self.lb_error.setText("La entrada no es un numero")
            else:
                self.lb_error.setText("Reconecte arduino")
        else:
            self.lb_error.setText("Conecte arduino")

    def stop(self):
        if self.arduino != None:
            if self.arduino.isOpen():
                self.arduino.write("0".encode())
                self.lb_error.setText("")
                self.txt_obj.setText("")
                self.btn_connect.setEnabled(True)
            else:
                self.lb_error.setText("Led reconecte arduino")
        else:
            self.lb_error.setText("Conecte arduino")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())