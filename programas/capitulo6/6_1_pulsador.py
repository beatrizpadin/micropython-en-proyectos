"""
MICROPYTHON EN PROYECTOS
Beatriz Padín / Adriana Dapena
Capítulo 6: Lámpara de señales
---------------------------------------
Se comprueba si el pulsador se está pulsando o no.
"""

from machine import Pin
from time import sleep_ms

# Pulsador en el GPIO17
PULSADOR = Pin(17, Pin.IN, Pin.PULL_UP)

while True:
    if PULSADOR.value() == 1:
        print("No se está pulsando el botón")
    else:
        print("Se está pulsando el botón")
    sleep_ms(200)