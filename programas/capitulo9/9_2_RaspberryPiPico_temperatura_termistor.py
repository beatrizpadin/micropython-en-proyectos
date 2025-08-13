"""
MICROPYTHON EN PROYECTOS
Beatriz Padín / Adriana Dapena
Capítulo 9: Cambio climático
---------------------------------------
Se lee la temperatura con un termistor.
- Termistor NTC de 10 kΩ a 25 ℃ / 298.15 K, con B = 3950 K.
- El termistor está conectado en serie con una resistencia de 10 kΩ.
https://learn.adafruit.com/thermistor/using-a-thermistor
"""

from machine import Pin, ADC
from time import sleep
from math import log

# Termistor conectado al GPIO28
SENSOR = ADC(Pin(28))

# Características del termistor
T0 = 298.15
R0 = 10000
B = 3950

# Resistencia del divisor de voltaje
Rs = 10000


while True:
    # Lectura del ADC (valor bruto)
    lectura = SENSOR.read_u16()

    # Resistencia
    R = Rs/(65535/lectura - 1)

    # Temperatura (en kelvins)
    T = 1/(1/T0 + 1/B*log(R/R0))

    # Temperatura (en grados centígrados)
    T = T - 273.15
    print(round(T,1))

    sleep(1)