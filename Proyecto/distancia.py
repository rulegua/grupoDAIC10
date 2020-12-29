import sys
import time
from grove.gpio import GPIO
import time
 

class SensorDistancia(object):
	
	
	def __init__(self, pin):
		self.distancia = GPIO(pin)
 
	def _get_distance(self):
		usleep = lambda x: time.sleep(x / 1000000.0)
 
		_TIMEOUT1 = 1000
		_TIMEOUT2 = 10000
	
		self.distancia.dir(GPIO.OUT)
		self.distancia.write(0)
		usleep(2)
		self.distancia.write(1)
		usleep(10)
		self.distancia.write(0)
 
		self.distancia.dir(GPIO.IN)

		t0 = time.time()
		count = 0
		while count < _TIMEOUT1:
			if self.distancia.read():
				break
			count += 1
		if count >= _TIMEOUT1:
			return None

		t1 = time.time()
		count = 0
		while count < _TIMEOUT2:
			if not self.distancia.read():
				break
			count += 1
		if count >= _TIMEOUT2:
			return None

		t2 = time.time()

		dt = int((t1 - t0) * 1000000)
		if dt > 530:
			return None

		distance = ((t2 - t1) * 1000000 / 29 / 2)    # cm

		return distance

	def get_distance(self):
		while True:
			dist = self._get_distance()
			if dist:
				return dist
 

 
# def main():
	# sensor = sensorDistancia(5)
 
    # print('Detecting distance...')
    # while True:
        # print('{} cm'.format(sensor.get_distance()))
        # time.sleep(1)
 
# if __name__ == '__main__':
    # main()
