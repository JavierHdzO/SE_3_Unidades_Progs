import serial as connector #para conectar con Arduino
import sys
import PyQt5
from PyQt5 import uic, QtWidgets

qtCreatorFile = "ProgramaT5.ui"  # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = PyQt5.uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals y Configuraciones Iniciales
        self.btn_Conectar.clicked.connect(self.conectar)
   #     self.btn_Apagar.clicked.connect(self.accion)
        self.btn_U1_1.clicked.connect(self.leds)
        self.btn_U1_2.clicked.connect(self.leds)
        self.btn_U1_3.clicked.connect(self.leds)
        self.btn_U1_4.clicked.connect(self.leds)
        self.btn_U1_5.clicked.connect(self.leds)
        self.btn_U1_6.clicked.connect(self.leds)
        self.btn_U1_7.clicked.connect(self.leds)
        self.btn_U1_8.clicked.connect(self.leds)
        self.btn_U1_9.clicked.connect(self.leds)
        self.btn_U1_10.clicked.connect(self.leds)
        self.btn_Apagar.clicked.connect(self.lowLeds)
        self.btn_Apagar.setEnabled(False)
        self.arduino = None #null en java


    # Área de los Slots
    def conectar(self):
        if self.arduino == None:
            com = "COM"+ self.txt_com.text()
        #    self.txt_com.setEnabled(False)
            self.arduino =  connector.Serial(com, baudrate=9600, timeout=1)  #Establece la conexion por primera vez
            print("Conexión Inicializada")
            self.btn_Apagar.setEnabled(True)
            self.btn_Conectar.setText("DESCONECTAR")
        elif self.arduino.isOpen(): ##otra opción: checar que el texto del boton sea desconectar
            self.btn_Conectar.setText("RECONECTAR")
            self.arduino.close()
            print("Conexion Cerrada")
            self.btn_Apagar.setEnabled(False)
        else:
            self.btn_Conectar.setText("DESCONECTAR")
            self.arduino.open()
            print("Conexion Reconectada")
            self.btn_Apagar.setEnabled(True)



    def accion(self):
        if self.arduino != None:
            if self.arduino.isOpen():  ##otra opción: checar que el texto del boton sea desconectar
                self.arduino.write("1".encode())
                print("El dato ha sido enviado correctamente")
            else:
                print("La conexión esta cerrada actualmente")
        else:
            print("Aun no se ha realizado la conexion con Arduino")


    def leds(self):
        index =int(self.sender().text()) -1
        if self.arduino != None:
            if self.arduino.isOpen():
                archivo = open("ProgramaT5.csv")
                contenedorArchivo = archivo.readlines()
                #print(contenedorArchivo)
                print(index)
                archivoProcesado = [ i.split(",") for i in contenedorArchivo]

                preferencia = [ int(i) for i in archivoProcesado[index]]
                a = str(preferencia)
                a= a[1: len(a)-1]
                print(a)
                self.arduino.write(a.encode())


    def lowLeds(self):
        if self.arduino != None:
            if self.arduino.isOpen():
                self.arduino.write(" ".encode())
                self.arduino.close()
                self.btn_Apagar.setEnabled(False)
                self.btn_Conectar.setText("RECONECTAR")



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
