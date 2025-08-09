"""
MICROPYTHON EN PROYECTOS
Beatriz Padín / Adriana Dapena
Capítulo 10: Data logger
---------------------------------------
Se registra la temperatura medida por el sensor TMP36
con el ESP32 o el Arduino Nano ESP32.
Los datos se guardan en un archivo.
El led parapadea cada vez que se toma una medida.
"""

import os
from machine import Pin, ADC
from time import sleep, sleep_ms

# Sensor de temperatura TMP36 en el GPIO14
TMP36 = ADC(Pin(14))

# Led en el GPIO 18
LED = Pin(18, Pin.OUT, value=0)

# Tiempo entre medidas (s)
INTERVALO = 1

# Nombre del archivo de datos
nombre = "datos"
extension = "csv"
ARCHIVO = nombre + "." + extension
i = 1
while ARCHIVO in os.listdir():
    ARCHIVO = "{}({}).{}".format(nombre, i, extension)
    i += 1

# Medida de la temperatura
def medir_temperatura():
    i = 1
    suma = 0
    num = 20
    while i <= num:
        # ESP32, Arduino Nano ESP32
        voltaje = TMP36.read_uv()/1000000
        suma += voltaje
        i += 1
    voltaje_medio = suma/num
    temperatura = round((voltaje_medio - 0.5)*100, 1)
    return temperatura

# Escritura de la temperatura en el archivo
def escribir_temperatura():
    with open(ARCHIVO, "a") as archivo:
        archivo.write(str(medir_temperatura()))
        archivo.write("\n")

# Parpadeo del led
def parpadeo():
    LED.value(1)
    sleep_ms(50)
    LED.value(0)


while True:
    parpadeo()
    escribir_temperatura()
    sleep(INTERVALO)