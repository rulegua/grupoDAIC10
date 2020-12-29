import sys
from grove.gpio import GPIO

class SensorNivel:

	#Constructor de la clase Nivel
	#Pin: Numero del pin que ocupa el sensor de nivel en el sombrero
	def __init__(self, pin):
		self.nivel = GPIO(pin, GPIO.IN)


	#Funcion para comprobar el nivel del liquido desinfectante
	def comprobarNivel(self):
		if self.nivel.read() == 1:
			#Devuelve True si queda liquido 
			print("Hay agua")
			return True
		else:
			#Devuelve false si no queda liquido 
			print("No hay agua")
			return False
