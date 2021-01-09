import led
import presion
import nivel
import bocina
import distancia
import boton
import time

from influxdb import InfluxDBClient
import argparse




def main(host='localhost', port=8086):
	inicioJornada = time.time()
	
	"""Parametros para la BD"""
	user = "Ruben"
	password = "Ruben"
	dbname = "SafeJoin"
	
	cliente = InfluxDBClient(host,port,user,password,dbname)
	
	"""Creamos la BD"""
	cliente.create_database(dbname)
	
	contador = 0
	temporal = time.time()
	while True:	

		finalJornada = time.time()

		if((finalJornada - inicioJornada) >= 5):cd 	#Numero en segundos
			cliente.drop_database("SafeJoin")
			break

	    #Declaracion de sensores
		sensorNivel = nivel.SensorNivel(22)				#Pin 22
		sensorPresionSilla = presion.SensorPresion(24) 		#Pin 24
		sensorPresionMesa = presion.SensorPresion(26) 		#Pin 26
		sensorLed = led.SensorLed(12) 					#Pin 12
		sensorDistancia = distancia.SensorDistancia(5)	#Pin 5
		sensorBocina = bocina.SensorBocina(16)	#Pin 16
		#sensorBotonEntrada = boton.SensorBoton(18)	#Pin 18
		#sensorBotonSalida = boton.SensorBoton(24) #Pin 24
	     
	     
		#Caso de uso 1: Si no hay nadie en la mesa ni nada encima de la mesa
		tiempoA = time.time()
		tiempoB = temporal
		temporal = None
		if((sensorPresionSilla.presionado() == False) and (sensorPresionMesa.presionado() == False) and (tiempoA - tiempoB >= 6)):
			sensorLed.encender()
			print("Limpiando mesa...")
			
			mensaje = formato_json("mesa",1)
			cliente.write_points(mensaje)
			
			time.sleep(5)
			sensorLed.apagar()
			print("Mesa limpia!")
			
			mensaje = formato_json("mesa", 0)
			cliente.write_points(mensaje)
			
			tiempoB = time.time()
			
		temporal = tiempoB	
		
		#Caso de uso 2: Si no hay liquido desinfectante se avisa al encargado
		if(sensorNivel.comprobarNivel() == False):
			
			#Enviar al chronograf una alerta
			mensaje = formato_json("liquido", 0)
			cliente.write_points(mensaje)
		else:
			mensaje = formato_json("liquido", 1)
			cliente.write_points(mensaje)
		
		#Caso de uso 3: Si la otra mesa esta demasiado cerca se activa la bocina
		distSeguridad = 15 #Minimo 15 cm de separacion
		distActual = sensorDistancia.get_distance()
		
		if(distActual < distSeguridad):
			sensorBocina.encender()
		
		else:
			sensorBocina.apagar()

	    
		"""#Caso de uso 4: Si se supera el aforo del local se activa la bocina
		if(sensorBotonEntrada.estaPresionado() == True):
			contador += 1
			time.sleep(0.5)
			print(contador)
			mensaje = formato_json("aforo", contador)
			cliente.write_points(mensaje)
			
		if(sensorBotonSalida.estaPresionado() == True):
			contador -= 1
			time.sleep(0.5)
			print(contador)
			mensaje = formato_json("aforo", contador)
			cliente.write_points(mensaje)
			
		if(contador > 4):
			sensorBocina.encender()
		else:
			sensorBocina.apagar()"""
			



#Tabla: Nombre de la tabla (aforo, liquido, mesa)
#Cantidad: 0 o 1
def formato_json(tabla, cantidad):
	if(tabla == "aforo"):
		json_body = [
            {
                "measurement": "Aforo",               
                "fields": {
                    "Personas": float(cantidad),
                }
            }
        ]
		return json_body
		

	if(tabla == "liquido"):
		if(cantidad == 0):
			estado = "No hay suficiente"
		else:
			estado = "Suficiente"
		json_body = [
            {
                "measurement": "Liquido",               
                "fields": {
                    "Cantidad": int(cantidad),
                }
            }
        ]
		return json_body

	if(tabla == "mesa"):
		if(cantidad == 0):
			estado = "Limpia"
		else:
			estado = "Sucia"

		json_body = [
            {
                "measurement": "Mesa",               
                "fields": {
                    "Estado": str(estado),
                }
            }
        ]
		return json_body



def parse_args():

    """Parse the args."""
    parser = argparse.ArgumentParser(
        description='example code to play with InfluxDB')
    parser.add_argument('--host', type=str, required=False,
                        default='localhost',
                        help='hostname of InfluxDB http API')
    parser.add_argument('--port', type=int, required=False, default=8086,
                        help='port of InfluxDB http API')
    return parser.parse_args()


if __name__ == '__main__':
     args = parse_args()
     main(host=args.host, port=args.port)
     
