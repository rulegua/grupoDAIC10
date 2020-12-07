import sys
from grove.gpio import GPIO

class SensorLed:
	
	#Constructor de la clase led
	#Pin: Numero del pin que ocupa el led en el sombrero
	def __init__(self, pin):
		self.luz = GPIO(pin, GPIO.OUT)

	#Funcion para encender el led
	def encender(self):
		self.luz.write(1)

	
	#Funcion para apagar el led
	def apagar(self):
		self.luz.write(0)


	#Funcion para comprobar el estado de led
	def encendido(self):
		if self.luz.read() == 1:
			return True
		else:
			return False