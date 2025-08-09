"""
MICROPYTHON EN PROYECTOS
Beatriz Padín / Adriana Dapena
Capítulo 9: Cambio climático
---------------------------------------
Se lee el voltaje de salida del sensor TMP36
en el ESP32 o el Arduino Nano ESP32.
"""

from machine import Pin, ADC
from time import sleep

# Sensor de temperatura TMP36 conectado al GPIO14
TMP36 = ADC(Pin(14))

while True:
    # Lectura del voltaje en voltios
    voltaje = TMP36.read_uv()/1000000
    print(voltaje)
    sleep(1)