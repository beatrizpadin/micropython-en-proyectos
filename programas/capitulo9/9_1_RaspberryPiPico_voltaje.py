"""
MICROPYTHON EN PROYECTOS
Beatriz Padín / Adriana Dapena
Capítulo 9: Cambio climático
---------------------------------------
Se lee el voltaje de salida del sensor TMP36
en la Raspberry Pi Pico.
"""

from machine import Pin, ADC
from time import sleep

# Sensor de temperatura TMP36 conectado al GPIO28
TMP36 = ADC(Pin(28))

while True:
    # Lectura del voltaje en voltios
    lectura = TMP36.read_u16()
    voltaje = lectura*3.3/65535
    print(voltaje)
    sleep(1)