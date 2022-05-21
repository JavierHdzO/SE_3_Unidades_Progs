from pynput.keyboard import Key, Controller

teclado = Controller()

teclado.press('U')
teclado.press('A')
teclado.press('T')

teclado.release('U')
teclado.release('A')
teclado.release('T')

teclado.type("\nUAT")
#COM, CONECTAR