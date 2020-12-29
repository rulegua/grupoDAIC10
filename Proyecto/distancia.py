import sys
from grove.gpio import GPIO
import time

class SensorDistancia:


	#Constructor de la clase Distancia
	#Trigger: Numero del trigger que ocupa el sensor ultrasonico
	#Echo: Numero del echo que ocupa el sensor ultrasonico
	def __init__(self, trigger, echo):
		self.trigger = trigger
		self.echo = echo
		


	#Funcion para obtener distancia a un objeto
	def distancia(self):
		
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(self.trigger, GPIO.OUT)
		GPIO.setup(self.echo, GPIO.IN)
		
		GPIO.output(self.trigger, False)
		time.sleep(2)
		
		GPIO.output(self.trigger, True)
		
		time.sleep(0.00001)
		
		GPIO.output(self.trigger, False)
		
		StartTime = time.time()
		StopTime = time.time()
		
		while GPIO.input(self.echo) == 0:
			StartTime = time.time()
		
		while GPIO.input(self.echo) == 1:
			StopTime = time.time()
			
			
		TimeElapsed = StopTime - StartTime
		
		distance = TimeElapsed	/ 0.000058
		distance = round(distance, 2)
		
		GPIO.cleanup()
		
		return distance
			
			
