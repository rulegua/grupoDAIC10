import led
import presion
import time


def main():

	while True:	


	    #Declaracion de sensores
	    sensorPresion = presion.SensorPresion(22)
	    sensorLed = led.SensorLed(12)
	    sensorLed.encender()

if __name__ == "__main__":
    main()