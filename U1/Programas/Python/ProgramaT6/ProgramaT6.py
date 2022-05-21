import serial as connector #para conectar con Arduino
import sys
import PyQt5
from PyQt5 import uic, QtWidgets
from PyQt5.QtGui import QIntValidator

qtCreatorFile = "ProgramaT6.ui"  # Nombre del archivo aquí.

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
        self.txt_num1.setValidator(QIntValidator())
        self.txt_num2.setValidator(QIntValidator())
        self.txt_num1.textChanged.connect(self.isEmpty)
        self.txt_num2.textChanged.connect(self.isEmpty)
        self.btn_sumar.clicked.connect(self.sumar)
        self.btn_reset.clicked.connect(self.reset)
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


    def sumar(self):
        if self.arduino != None:
            if self.arduino.isOpen():
                if ("+" != self.txt_num1.text() != "-") \
                        and  ("+" != self.txt_num2.text() != "-") :
                    print("entro")
                    num1 = int(self.txt_num1.text())
                    num2 = int(self.txt_num2.text())
                    result = num1 + num2
                    if self.isCheck(result):
                        self.arduino.write("{0}".format(result).encode())
                        self.txt_result.setText(str(result))
                else:
                    self.lb_error.setText("No es un numero")



    def isCOM(self):
        self.btn_connect.setEnabled(True)
        if not self.txt_com.text().isnumeric():
            self.btn_connect.setEnabled(False)


    def isEmpty(self):
        self.btn_sumar.setEnabled(True)
        self.lb_error.setText("")
        if not (self.txt_num1.text().strip() and self.txt_num2.text().strip()):
            self.btn_sumar.setEnabled(False)


    def isCheck(self, result):
        if result >= 0 and result <= 255:
            if result <= 255:
                return True
            else:
                self.lb_error.setText("La suma supera 255 o es menor a 0")
                return False


    def reset(self):
        self.txt_num1.setText("")
        self.txt_num2.setText("")
        self.txt_result.setText("")
        self.lb_error.setText("")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())