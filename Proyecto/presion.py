import sys
from grove.gpio import GPIO

class SensorPresion:
	
	#Constructor de la clase presion
	#Pin: Numero del pin que ocupa el sensor de presion en el sombrero
	def __init__(self, pin):
		self.presion = GPIO(pin, GPIO.IN)

	#Funcion para comprobar si hay algo encima o no
	def presionado(self):
		if self.presion.read() == 1:
			return True
		else:
			return False