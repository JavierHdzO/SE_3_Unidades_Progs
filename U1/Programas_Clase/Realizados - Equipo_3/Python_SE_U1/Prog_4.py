import serial
import time

arduino = serial.Serial("COM3",baudrate=9600,timeout=1)
arduino.flush()


arduino.write("2".encode())
t = arduino.read()
arduino.close()

time.sleep(2)