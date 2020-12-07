import sys
#from grove.gpio import GPIO

class Led:
	def __init__(self, pin):
		self.luz = GPIO(pin, GPIO.OUT)


	def encender(self):
		luz.write(1)

	
	def apagar(self):
		luz.write(0)
