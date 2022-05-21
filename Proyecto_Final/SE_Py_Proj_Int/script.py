import serial as connector #para conectar con Arduino

import sys
import tecnicas
import time
from PyQt5 import uic, QtWidgets
from random import randint
import WebService.WineWebService as WineWS,\
    WebService.IrisWebService as IrisWS,\
    WebService.CancerWebService as CancerWS

from pygments.styles import arduino

qtCreatorFile = "interfazProyectoU3.ui"  # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals y Configuraciones Iniciales
        self.btn_conectar.clicked.connect(self.conectar)
        self.btn_start.clicked.connect(self.start)
        self.btn_delete.clicked.connect(self.deleteData)
        self.btn_read.clicked.connect(self.read)

        ##buttons disable before to start a connection
        self.btn_start.setEnabled(False)
        self.btn_delete.setEnabled(False)
        self.btn_read.setEnabled(False)
        self.comboBox_instancias.setEnabled(False)
        self.comboBox_tecnicas.setEnabled(False)
        self.instancias = {"Wine":"DatosDiscretizadosWine.csv", "Iris": "DatosDiscretizadosIris.txt", "Cancer":"breast-cancer-wisconsin.csv"}
        self.datosasolicitar = [13,4,9]
        self.tecnicas = ["KNN", "Asociador Lineal", "Navy Bayes"]
        self.comboBox_instancias.addItems(self.instancias)
        self.comboBox_tecnicas.addItems(self.tecnicas)
        self.arduino = None #null en java
        self.pruebas = []
        self.pruebaAux = []

    """Para recibir los datos desde arduino se necesita primero enviarle la cantidad de datos requeridos"""
    def read(self):
        #print(self.instancias[self.comboBox_instancias.currentText()])
        self.btn_read.setEnabled(False)
        self.comboBox_instancias.setEnabled(False)
        self.comboBox_tecnicas.setEnabled(False)

        #arreglo donde se guardan los casos prueba
        self.arduino.write("A{0}G".format(self.datosasolicitar[self.comboBox_instancias.currentIndex()]).encode())
        str_recibido = ""


        """Se le da instruccion al usuario y se deshabilita el boton"""

        #LECTURA DEL CASO PRUEBA
        while True:
            str_recibido += self.arduino.readline().decode()
            if  str_recibido != "":
                if str_recibido[-3] == "G":
                    break

        str_recibido = str_recibido[1:-3]#se quitan a y G\r\n

        indexActualInst = self.comboBox_instancias.currentIndex()

        if indexActualInst == 0 : #para indice de instancia Wine
            datos = str_recibido.split(",")
            casoPrueba = list(map(int, datos))
            WineWS.POST_InsertWine(casoPrueba) #Llama al webService de Wine y guarda el caso
        elif indexActualInst == 1:
            datos = str_recibido.split(",")
            casoPrueba = list(map(int, datos[:-1]))
            casoPrueba.append(datos[-1])
            IrisWS.POST_InsertIris(casoPrueba) #Llama al webService de Iris y guarda el caso
        else:
            datos = str_recibido.split(",")
            casoPrueba = list(map(int, datos))
            CancerWS.POST_InsertCancer(casoPrueba) #Llama al webService de Cancer y guarda el caso

        listWidgetItem = QtWidgets.QListWidgetItem(str_recibido)
        self.listWidget_results.addItem(listWidgetItem)


        ## AQUI SE CONSULTA EL WEB SERVICE PARA CONSTRUIR LA MATRIZ DE CASOS PRUEBA

        if indexActualInst == 0:
            querySelectAll = WineWS.GET_SelectAllTestWine()
        elif  indexActualInst == 1:
            querySelectAll = IrisWS.GET_SelectAllTestIris()
        else:
            querySelectAll = CancerWS.GET_SelectAllTestCancer()
            print(querySelectAll)
        print(querySelectAll)
        querySelectAll = [list(x.values()) for x in querySelectAll]
        print(querySelectAll)



        self.pruebas = querySelectAll[:]
        self.pruebaAux = self.pruebas[:]
        self.btn_read.setEnabled(True)
        self.btn_start.setEnabled(True)
        self.comboBox_tecnicas.setEnabled(True)


    def start(self):

        claseDevuelta = []
        tecnicaSeleccionada = self.comboBox_tecnicas.currentIndex()
        instanciaSeleccionada = self.comboBox_instancias.currentText()
        indexIntanciaSeleccionada = self.comboBox_instancias.currentIndex()
        print(tecnicaSeleccionada)
        if tecnicaSeleccionada == 0:
            claseDevuelta = tecnicas.KNN(self.pruebas, indexIntanciaSeleccionada)

        elif tecnicaSeleccionada == 1:
            claseDevuelta =  tecnicas.asociadorLineal(self.pruebas, indexIntanciaSeleccionada)
        else:
            claseDevuelta = tecnicas.naiveBayes(self.pruebas, indexIntanciaSeleccionada)
        self.pruebas = self.pruebaAux[:]
        self.btn_delete.setEnabled(True)

        """ENVIO DE RESPUESTAS A ARDUINO"""
        for clase in claseDevuelta:
            if instanciaSeleccionada == "Wine":
                if clase == "1" or clase == 1:
                    self.arduino.write("A{0}G".format("100").encode())
                elif  clase == "2" or clase == 2:
                    self.arduino.write("A{0}G".format("010").encode())
                else:
                    self.arduino.write("A{0}G".format("001").encode())
            elif instanciaSeleccionada == "Iris":
                clase = clase.replace("\n","")
                if clase == "Iris-virginica":
                    self.arduino.write("A{0}G".format("100").encode())
                elif clase == "Iris-versicolor":
                    self.arduino.write("A{0}G".format("010").encode())
                else:
                    self.arduino.write("A{0}G".format("001").encode())
            else:
                if clase == "2" or clase == 2:
                    self.arduino.write("A{0}G".format("100").encode())
                else:
                    self.arduino.write("A{0}G".format("001").encode())
            time.sleep(2)


    """ CODIFICACION iris"""
    # iris virginica - 100
    # versicolor - 010
    # setosa - 001

    """CODIFICACION WINE"""
    # 1 = 100
    # 2 = 010
    # 3 = 001

    """CODIFICACION CANCER"""
    # 2 = 100
    # 4 = 001

    def deleteData(self):
        WineWS.DELETE_AllTestWine()
        IrisWS.DELETE_AllTestIris()
        CancerWS.DELETE_AllTestCancer()
        self.listWidget_results.clear()
        self.btn_start.setEnabled(False)
        self.pruebas.clear()
        self.comboBox_instancias.setEnabled(True)
        self.comboBox_tecnicas.setEnabled(True)

    # Área de los Slots
    def conectar(self):
        if self.arduino == None:
            try:
                WineWS.DELETE_AllTestWine()
                IrisWS.DELETE_AllTestIris()
                CancerWS.DELETE_AllTestCancer()
                com = "COM"+ self.txt_com.text()
                self.txt_com.setEnabled(False)
                self.arduino =  connector.Serial(com, baudrate=9600, timeout=1)  #Establece la conexion por primera vez
                print("Conexión Inicializada")
                self.btn_conectar.setText("DESCONECTAR")

                #buttons enabled
                self.btn_read.setEnabled( True)
                self.comboBox_instancias.setEnabled(True)
                self.comboBox_tecnicas.setEnabled(True)
            except:
                pass

        elif self.arduino.isOpen(): ##otra opción: checar que el texto del boton sea desconectar
            self.btn_conectar.setText("RECONECTAR")
            self.arduino.close()
            print("Conexion Cerrada")

            ##buttons disable before to start a connection
            self.btn_start.setEnabled(False)
            self.btn_delete.setEnabled(False)
            self.btn_read.setEnabled(False)
            self.deleteData()
            self.comboBox_instancias.setEnabled(False)
            self.comboBox_tecnicas.setEnabled(False)
        else:
            self.btn_conectar.setText("DESCONECTAR")
            self.arduino.open()
            print("Conexion Reconectada")
            self.deleteData()
            #buttons enabled
            self.btn_read.setEnabled( True)
            self.comboBox_instancias.setEnabled(True)
            self.comboBox_tecnicas.setEnabled(True)



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())