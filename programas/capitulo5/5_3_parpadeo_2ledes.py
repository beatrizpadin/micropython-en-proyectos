"""
MICROPYTHON EN PROYECTOS
Beatriz Padín / Adriana Dapena
Capítulo 5: Señalización marítima
---------------------------------------
Se encienden dos ledes de manera intermitente.
El tiempo se controla con la función sleep().
"""

from machine import Pin
from time import sleep

# Led verde en el GPIO18, inicialmente encendido
LED_VERDE = Pin(18, Pin.OUT, value=1)

# Led rojo en el GPIO21, inicialmente apagado
LED_ROJO = Pin(21, Pin.OUT, value=0)

# Tiempo entre destellos (s)
INTERVALO = 1

while True:
    # Los ledes parpadean alternativamente
    LED_VERDE.value(not LED_VERDE.value())
    LED_ROJO.value(not LED_ROJO.value())
    sleep(INTERVALO)