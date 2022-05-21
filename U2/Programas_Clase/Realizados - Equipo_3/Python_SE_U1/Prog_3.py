import serial as connector

arduino = connector.Serial("COM3",baudrate=9600,timeout=1)
valor = arduino.readline()
valor = valor.decode()

print(valor)