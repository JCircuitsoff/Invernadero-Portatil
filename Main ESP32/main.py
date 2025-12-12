from machine import Pin,ADC
from time import sleep
import dht
#Variables
sensorLuz = Pin(22,Pin.IN)
actuadorLuz = Pin (25,Pin.OUT)

sensorRiego = ADC(Pin(34))
actuadorRiego = Pin(23,Pin.OUT)

sensorNivel= ADC(Pin(35))
actuadorNivel = Pin(18, Pin.OUT)

sensorT = dht.DHT11(Pin(4))
actuadorT = Pin(27,Pin.OUT)

while True:
  #Circuito Luz
  estado = sensorLuz.value()
    
  if estado == 1:
     actuadorLuz.value(0)
  else:
     actuadorLuz.value(1)
          
  #Circuito Riego        
  valor = sensorRiego.read_u16()
  humedad = ((valor-40100)/25435)*100
  porcentaje = abs(humedad)
  porcentaje = abs(porcentaje -100)
    
  if porcentaje >=75:
     actuadorRiego.value(1)
  else:
     actuadorRiego.value(0)

  #Circuito nivel de agua
  valor = sensorNivel.read_u16()
  porcentaje = (valor*100)/65535
    
  if porcentaje >= 75:
        actuadorNivel.value(0)
  else:
        actuadorNivel.value(1)
  #Circuito temperatura
  try:
    sensorT.measure()
    temperatura = sensorT.temperature()
    print ("Temperatura: ", temperatura, " °C")
    
    if temperatura >= 10 and temperatura <= 21:
      actuadorT.value(1)
    else:
      actuadorT.value(0)
    
  except OSError:
    print ("Fallo al leer el DHT11") 
  sleep(2)
