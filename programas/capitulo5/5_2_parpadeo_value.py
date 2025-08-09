from machine import Pin
from time import sleep_ms

# Led conectado en el GPIO18, inicialmente apagado
LED = Pin(18, Pin.OUT, value=0)

# Tiempo de encendido y apagado
INTERVALO = 100

while True:
    # Se enciende y apaga el led
    LED.value(not LED.value())
    sleep_ms(INTERVALO)