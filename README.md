# SafeJoin
El objetivo de este proyecto es facilitar el trabajo a los hosteleros frente a las medidas de la COVID-19 mediante del uso del Internet de las Cosas (IoT). 

* Estado del proyecto: Finalizado

## Pre-requisitos 📋
* Python3
* Chronograf
* InfluxDB
* Kapacitor

## Hardware necesario:
* Raspberry Pi 3 (Model B+)
* LED Socket Kit v1.5
* Moisture Sensor v1.4
* Buzzer v1.2
* Button(P) v1.2a x2
* Touch v1.1 x2
* Grove Ultrasonic Ranger v2.0

## Usabilidad 
Clonar el repositorio:
```bash
git clone https://github.com/rulegua/grupoDAIC10.git
```
En la carpeta Proyecto/ ejecutar el siguiente comando:
```bash
python main.py
```
Para visualizar el monitoreo acceder al [link](http://localhost:8888/sources/1/dashboards/2?refresh=Paused&lower=now%28%29%20-%2015m)

## Construido con 🛠️
* [InfluxDB](https://www.influxdata.com/)

## Autores
* Rubén Legarreta - (https://github.com/rulegua)
* Roberto Martínez-Guisasola - (https://github.com/Robertoguisasola)
