import sys
from grove.gpio import GPIO

class SensorBoton:
	
	#Constructor de la clase led
	#Pin: Numero del pin que ocupa el led en el sombrero
	def __init__(self, pin):
		self.boton = GPIO(pin, GPIO.IN)

	def estaPresionado(self):
		if (self.boton.read() == 1):
			return True
