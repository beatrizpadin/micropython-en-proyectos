from machine import Pin
from time import sleep

# Led conectado en el GPIO18
LED = Pin(18, Pin.OUT)

while True:
    # Led encendido
    LED.on()    
    print("Encendido")
    sleep(1)
    
    # Led apagado
    LED.off()   
    print("Apagado")
    sleep(1)