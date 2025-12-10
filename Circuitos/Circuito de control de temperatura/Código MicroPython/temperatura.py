from machine import Pin
import dht
from time import sleep

sensor = dht.DHT11(Pin(4))
actuador = Pin(27,Pin.OUT)

while True:
    try:
        sensor.measure()
        temperatura = sensor.temperature()
        print ("Temperatura: ", temperatura, " °C")
    
        if temperatura >= 10 and temperatura <= 21:
            actuador.value(1)
      
        else:
            actuador.value(0)
    
    except OSError:
        print ("Fallo al leer el DHT11")
    
    sleep(2)
         
