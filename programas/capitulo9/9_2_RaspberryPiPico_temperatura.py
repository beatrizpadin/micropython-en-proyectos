"""
MICROPYTHON EN PROYECTOS
Beatriz Padín / Adriana Dapena
Capítulo 9: Cambio climático
---------------------------------------
Se lee la temperatura medida por el sensor TMP36
con la Raspberry Pi Pico.
"""

from machine import Pin, ADC
from time import sleep

# Sensor de temperatura TMP36 conectado al GPIO28
TMP36 = ADC(Pin(28))

while True:
    # Temperatura en grados centígrados
    voltaje = TMP36.read_u16()*3.3/65535
    temperatura = (voltaje - 0.5)*100
    print(round(temperatura, 1))
    sleep(1)