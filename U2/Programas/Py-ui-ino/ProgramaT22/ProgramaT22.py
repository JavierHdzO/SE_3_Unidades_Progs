import numpy as np
import serial as connector #para conectar con Arduino
import sys
import PyQt5
from PyQt5 import uic, QtWidgets
from PyQt5.QtGui import QIntValidator

qtCreatorFile = "ProgramaT22.ui"  # Nombre del archivo aquí.

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

        self.txt_array.setValidator(QIntValidator())
        self.txt_array.textChanged.connect(self.isEmpty)

        self.btn_start.clicked.connect(self.start)
        self.btn_stop.clicked.connect(self.stop)

        self.label_3.setVisible(False)

        self.arduino = None #null en java


    # Área de los Slots
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
        if not self.txt_array.text().isnumeric():
            self.btn_connect.setEnabled(False)
            self.lb_error.setText("")


    def isEmpty(self):
        self.btn_start.setEnabled(True)
        self.lb_error.setText("")
        if not self.txt_array.text().strip():
            self.btn_start.setEnabled(False)

    def start(self):
        num = self.txt_array.text().strip();
        if self.arduino != None:
            if self.arduino.isOpen():
                if "+" != num != "-":
                    numObj = int(num)
                    if numObj >= 0 and numObj <= 255:
                        VectorB = np.random.randint(0, 2, size=(numObj, 8))
                        data = self.FO(VectorB);
                        self.lb_vectors.setText(str(VectorB))
                        self.lb_show.setText(data)
                        self.arduino.write("{0}".format(data).encode())
                        self.btn_connect.setEnabled(False)
                        self.btn_start.setEnabled(False)
                        self.label_3.setVisible(True)
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
                self.arduino.write("A00000000G".encode())
                self.lb_error.setText("")
                self.txt_array.setText("")
                self.btn_connect.setEnabled(True)
                self.label_3.setVisible(False)
                self.lb_show.setText("")
                self.lb_vectors.setText("")
            else:
                self.lb_error.setText("Led reconecte arduino")
        else:
            self.lb_error.setText("Conecte arduino")

    def FO(self, Vector):
        R = []
        for i in range(len(Vector)):
            cont = 0
            print("\n\nVector [{ite}]".format(ite=i + 1))
            for j in range(len(Vector[i])):
                if Vector[i][j] == 1:
                    cont += 1
                print(Vector[i][j].tolist(), end=' ')

            print("\nLa suma de 1s en el vector [{vect}] es: {conta}".format(vect=i + 1, conta=cont))
            R.append(cont)

        data = str(Vector[R.index(np.max(R))])
        data = data[1:len(data) - 1]
        data = data.replace(" ", "")
        data = "A" + data + "G"
        print(data)
        return data


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
