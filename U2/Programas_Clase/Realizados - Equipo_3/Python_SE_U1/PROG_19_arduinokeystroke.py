import serial as s
import time as t

arduino = s.Serial("COM3", baudrate=9600, timeout=1)

from pynput.keyboard import Key, Controller

teclado = Controller()

while True:
    val = arduino.readline().decode()
    val = val.replace("\n", "")
    val = val.replace("\r", "")

    print(val)

    if val == "1":
        teclado.press('A')
        teclado.release('A')
    else:
        pass

    t.sleep(.1)