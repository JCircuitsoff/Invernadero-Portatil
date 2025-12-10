from machine import Pin
from time import sleep

sensorLuz = Pin(22,Pin.IN)
actuadorLuz = Pin (25,Pin.OUT)

while True:
  estado = sensorLuz.value()
  sleep(1)
    
  if estado == 1:
     actuadorLuz.value(0)
  else:
     actuadorLuz.value(1)
          
