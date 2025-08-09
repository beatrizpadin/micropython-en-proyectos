"""
MICROPYTHON EN PROYECTOS
Beatriz Padín / Adriana Dapena
Capítulo 8: Música arcade
---------------------------------------
Se genera una nota de 440 Hz durante 2 segundos.
"""

from machine import Pin, PWM
from time import sleep

# Altavoz en GPIO18
# Se incializa la señal PWM
ALTAVOZ = PWM(Pin(18), duty_u16=32768)

# Se establece la frecuencia en 440 Hz
ALTAVOZ.freq(440)
sleep(2)

# Se desactiva la señal
ALTAVOZ.deinit()