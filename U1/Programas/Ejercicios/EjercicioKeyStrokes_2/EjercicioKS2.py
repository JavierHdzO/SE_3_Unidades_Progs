import serial as connector  # para conectar con Arduino
import sys
import PyQt5
import threading
from pynput.keyboard import Key, Controller



from PyQt5 import uic, QtWidgets

qtCreatorFile = "Ejercicio2_Key.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = PyQt5.uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals y Configuraciones Iniciales
        self.btn_connect.clicked.connect(self.conectar)
        self.txt_com.textChanged.connect(self.isCOM)
        self.arduino = None  # null en java
        self.flag = True
        self.threadLectura = None
        self.teclado = Controller()

    # Área de los Slots
    def conectar(self):

        try:
            if self.arduino == None:
                com = "COM" + self.txt_com.text()
                self.arduino = connector.Serial(com, baudrate=9600, timeout=1)  # Establece la conexion por primera vez
                print("Conexión Inicializada")
                self.lb_error.setText("");
                self.threadLectura = threading.Thread(name="thread1", target=self.lectura)
                self.threadLectura.start()
                self.btn_connect.setText("DESCONECTAR")
            elif self.arduino.isOpen():  ##otra opción: checar que el texto del boton sea desconectar
                self.btn_connect.setText("RECONECTAR")
                self.arduino.close()
                self.flag = False
                print("Conexion Cerrada")
            else:
                self.btn_connect.setText("DESCONECTAR")
                self.arduino.open()
                self.lb_error.setText("");
                self.flag = True
                self.threadLectura = threading.Thread(name="thread1", target=self.lectura)
                self.threadLectura.start()
                print("Conexion Reconectada")
        except Exception as e:
            self.flag = False
            print(e)

    def isCOM(self):  # La funci[on isCom sirve para saber si el valor del LineEdit del COM es un numero
        self.btn_connect.setEnabled(True)  # habilita el boton btn-conectar
        if not self.txt_com.text().isnumeric():  # saber si el texto es numero.
            self.btn_connect.setEnabled(False)  # desHabilita el boton connect

    def lectura(self):
        try:
            while True:
                if not self.flag:
                    break
                valor = self.arduino.readline().decode()
                valor = valor.replace("\n", "")
                valor = valor.replace("\r", "")

                self.ls_valores.addItem(valor)
                self.ls_valores.setCurrentRow(self.ls_valores.count() -1)

                if valor == "14":
                    self.teclado.press('A')
                    self.teclado.release('A')
                elif valor == "13":
                    self.teclado.press('W')
                    self.teclado.release('W')
                elif valor == "12":
                    self.teclado.press('S')
                    self.teclado.release('S')
                elif valor == "11":
                    self.teclado.press('D')
                    self.teclado.release('D')
                elif valor == "10":
                    self.teclado.press('F')
                    self.teclado.release('F')


        except Exception as e:
            self.arduino.close()
            self.flag = False
            self.btn_connect.setText("RECONECTAR")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
