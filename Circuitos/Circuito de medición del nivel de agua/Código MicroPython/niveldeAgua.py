from machine import Pin,ADC
from time import sleep

sensor= ADC(Pin(35))
actuador = Pin(18, Pin.OUT)

while True:
    valor = sensor.read_u16()
    porcentaje = (valor*100)/65535
    print("Lectura: ",porcentaje, "%")
    sleep(0.5)
    
    if porcentaje >= 75:
        actuador.value(0)
    else:
        actuador.value(1)
    
        
        