"""
MICROPYTHON EN PROYECTOS
Beatriz Padín / Adriana Dapena
Capítulo 6: Lámpara de señales
---------------------------------------
Se enciende y apaga el led usando un pulsador.
El estado del led cambia de encendido a apagado, y viceversa,
cada vez que se pulsa el botón.
"""

from machine import Pin
from time import sleep_ms

# Pulsador en el GPIO17
PULSADOR = Pin(17, Pin.IN, Pin.PULL_UP)

# Led en el GPIO18
LED = Pin(18, Pin.OUT, value=0)

while True:
    if PULSADOR.value() == 0:
        LED.value(not LED.value())
    sleep_ms(200)