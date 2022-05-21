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

        # Área de los Signals y Configuraciones Iniciales
        self.btn_connect.clicked.connect(self.conectar)
        self.txt_com.textChanged.connect(self.isCOM)
        self.txt_word.textChanged.connect(self.isEmpty)
        self.btn_init.clicked.connect(self.getAscii)
        self.arduino = None #null en java


    # Área de los Slots
    def conectar(self):
        if self.arduino == None:
            com = "COM"+ self.txt_com.text()
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



    def isCOM(self): #La funci[on isCom sirve para saber si el valor del LineEdit del COM es un numero
        self.btn_connect.setEnabled(True) #habilita el boton btn-conectar
        if not self.txt_com.text().isnumeric(): # saber si el texto es numero.
            self.btn_connect.setEnabled(False) # desHabilita el boton connect

    def isEmpty(self): #Verifica si el LineEdit esta vacio
        self.btn_init.setEnabled(True) # deshabilita el boton bt-init
        if not self.txt_word.text().strip(): #verifica si la cadena esta vacia
            self.btn_init.setEnabled(False)

    def getAscii(self): #Obtiene el valor ascii de cada letra de la palbra ingresada
        if self.arduino != None: #Saber si la varaible arduino es nula
            if self.arduino.isOpen(): # Saber si la varaible arduino tiene una conexion abierta
                if not self.txt_word.text().isnumeric(): #Si el lineEdit txt_word es un numero
                    charArray = [ ord(w) for w in self.txt_word.text().strip()] #la funcion ord regresa el valor ascii dell caracter
                    a = str(charArray) # " 112,101,114,114,111]"  convierte la lista en string
                    a = a[1: len(a) - 1] # "112,101,114,114,111"  quita los corchetes del string
                    self.arduino.write(a.encode()) # Manda los valores a arduino
            else:
                self.lb_error.setText("La conexion con arduino esta cerrada")
        else:
            self.lb_error.setText("No se ha establecido conexion con arduino")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
