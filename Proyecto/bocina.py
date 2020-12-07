import sys
from grove.gpio import GPIO

class SensorBocina:
	
	#Constructor de la clase Bocina
	#Pin: Numero del pin que ocupa la bocina en el sombrero
	def __init__(self, pin):
		self.bocina = GPIO(pin, GPIO.OUT)

	#Funcion para encender la bocina
	def encender(self):
		self.bocina.write(1)

	
	#Funcion para apagar la bocina
	def apagar(self):
		self.bocina.write(0)