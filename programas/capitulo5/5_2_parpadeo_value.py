"""
MICROPYTHON EN PROYECTOS
Beatriz Padín / Adriana Dapena
Capítulo 5: Señalización marítima
---------------------------------------
Se enciende un led de manera intermitente
usando el método value() y el operador not.
"""

from machine import Pin
from time import sleep_ms

# Led conectado en el GPIO18, inicialmente apagado
LED = Pin(18, Pin.OUT, value=0)

# Tiempo de encendido y apagado (ms)
INTERVALO = 100

while True:
    # Se enciende y apaga el led
    LED.value(not LED.value())
    sleep_ms(INTERVALO)