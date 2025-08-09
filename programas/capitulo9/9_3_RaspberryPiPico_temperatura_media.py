"""
MICROPYTHON EN PROYECTOS
Beatriz Padín / Adriana Dapena
Capítulo 9: Cambio climático
---------------------------------------
Se lee la temperatura medida por el sensor TMP36
con la Raspberry Pi Pico.
Para suavizar las medidas se calcula la media de 20 valores.
"""

from machine import Pin, ADC
from time import sleep_ms

# Sensor de temperatura TMP36 conectado al GPIO14
TMP36 = ADC(Pin(14))

def voltaje_medio():
    i = 1
    suma = 0
    num = 20
    while i <= num:
        voltaje = TMP36.read_u16()*3.3/65535
        suma += voltaje
        i += 1
    media = suma/num
    return media    

while True:
    temperatura = (voltaje_medio() - 0.5)*100
    print(round(temperatura, 1))
    sleep_ms(500)