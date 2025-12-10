from machine import Pin,ADC
from time import sleep

sensorRiego = ADC(Pin(34))
actuadorRiego = Pin(23,Pin.OUT)

while True:
      valor = sensorRiego.read_u16()
      humedad = ((valor-40100)/25435)*100
      porcentaje = abs(humedad)
      porcentaje = abs(porcentaje -100)
      sleep(0.5)
    
      if porcentaje >=75:
          actuadorRiego.value(1)
      else:
          actuadorRiego.value(0)

