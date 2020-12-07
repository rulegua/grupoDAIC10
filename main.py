import led

def main():

	while True:	
	    print("Probando led!")
	    bombilla = led.Led(12)
	    print(bombilla.luz)
	    bombilla.encender()

if __name__ == "__main__":
    main()