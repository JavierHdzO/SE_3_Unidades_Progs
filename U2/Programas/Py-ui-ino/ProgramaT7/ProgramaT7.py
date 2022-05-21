import serial as connector #para conectar con Arduino
import sys
import PyQt5
from PyQt5 import uic, QtWidgets
from PyQt5.QtGui import QIntValidator

qtCreatorFile = "ProgramaT7.ui"  # Nombre del archivo aquí.

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
        self.txt_led.setValidator(QIntValidator())
        self.txt_led.textChanged.connect(self.isEmpty)
        self.btn_start.clicked.connect(self.start)
        self.btn_stop.clicked.connect(self.stop)
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
        self.btn_start.setEnabled(True)
        self.lb_error.setText("")
        if not self.txt_led.text().strip():
            self.btn_start.setEnabled(False)

    def start(self):
        led = self.txt_led.text().strip();
        if self.arduino != None:
            if self.arduino.isOpen():
                if "+" != led != "-":
                    ledN = int(led)
                    if ledN >= 1 and ledN <= 8:
                        self.arduino.write("{0}".format(ledN -1).encode())
                        self.btn_connect.setEnabled(False)
                        self.btn_start.setEnabled(False)
                    else:
                        self.lb_error.setText("LED fuera del rango[1-8]")
                else:
                    self.lb_error.setText("LED no es un numero")
            else:
                self.lb_error.setText("Led reconecte arduino")
        else:
            self.lb_error.setText("Conecte arduino")

    def stop(self):
        if self.arduino != None:
            if self.arduino.isOpen():
                self.arduino.write("-1".encode())
                self.lb_error.setText("")
                self.txt_led.setText("")
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