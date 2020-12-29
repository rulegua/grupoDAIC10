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
	while True:	

		finalJornada = Time.time()

		if((finalJornada - inicioJornada) >= 10)	#Numero en segundos
			cliente.drop_database("SafeJoin")
			break

	    #Declaracion de sensores
	    sensorNivel = nivel.SensorNivel(22) 	#Pin 22
	    sensorPresion = presion.SensorPresion(24) 	#Pin 24
	    # sensorLed = led.SensorLed(12) 		#Pin 12
	    sensorBocina = bocina.SensorBocina(12)	#Pin 5
	    sensorBoton = boton.SensorBoton(5)
	     
	     
	     #sensorBocina.apagar()
	    #Caso de uso 1: Si no hay nadie en la mesa y
	    # if(sensorPresion.presionado() == False):	#Aqui falta la condicion del sensor laser
		# sensorLed.encender()
		# print("Limpiando mesa...")
		# time.sleep(5)
		# sensorLed.apagar()
		# print("Mesa limpia!")
		
	    # #Caso de uso 2: Si no hay liquido desinfectante se avisa al encargado
	    if(sensorNivel.comprobarNivel() == False):
			
			#Enviar al chronograf una alerta
			mensaje = formato_json("liquido", 0)
			cliente.write_points(mensaje)
		else:
			mensaje = formato_json("liquido", 1)
			cliente.write_points(mensaje)

	    
	    #Caso de uso 3: Si se supera el aforo del local se activa la bocina
	    if(sensorBoton.estaPresionado() == True):
		    contador += 1
		     
		    time.sleep(0.5)
		    print(contador)

	     
	    if(contador > 3):
		    sensorBocina.encender()
		    time.sleep(2)
	     
		    print("Aforo actual: ")
		    aforo = int(input())
	     
		    if(aforo <= 3):
				sensorBocina.apagar()
				contador = aforo



#Tabla: Nombre de la tabla (aforo, líquido, mesa)
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
                    "Cantidad": string(estado),
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
                    "Estado": string(estado),
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
     
# if __name__ == "__main__":
    # main()
