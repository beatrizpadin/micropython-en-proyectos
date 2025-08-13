"""
MICROPYTHON EN PROYECTOS
Beatriz Padín / Adriana Dapena
Capítulo 10: Data logger
---------------------------------------
Se registra la temperatura medida por el termistor (ESP32/Arduino). 
Los datos se guardan en un archivo.
El led parapadea cada vez que se toma una medida.
TERMISTOR:
- Termistor NTC de 10 kΩ a 25 ℃ / 298.15 K, con B = 3950 K.
- El termistor está conectado en serie con una resistencia de 10 kΩ.
- https://learn.adafruit.com/thermistor/using-a-thermistor
"""

from machine import Pin, ADC
from time import sleep, sleep_ms
from math import log
import os


# Led en el GPIO 18
LED = Pin(18, Pin.OUT, value=0)

# Termistor en el GPIO14
SENSOR = ADC(Pin(14))

# Características del termistor
T0 = 298.15
B = 3950
R0 = 10000

# Resistencia del divisor de voltaje
Rs = 10000

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


def medir_temperatura():
    """
    Devuelve la temperatura medida por el termistor
    en grados centígrados.
    """
    # Lectura del ADC (valor bruto)
    lectura = SENSOR.read_u16()
    # Resistencia
    R = Rs/(65535/lectura - 1)
    # Temperatura (en kelvins)
    T = 1/(1/T0 + 1/B*log(R/R0))
    # Temperatura (en grados centígrados)
    T = T - 273.15
    return round(T, 1)


def escribir_temperatura():
    """
    Escribe en un archivo la temperatura
    medida por el termistor.
    """
    with open(ARCHIVO, "a") as archivo:
        archivo.write(str(medir_temperatura()))
        archivo.write("\n")


def parpadeo():
    """
    Enciende y apaga el led cada 50 ms. 
    """
    LED.value(1)
    sleep_ms(50)
    LED.value(0)


while True:
    parpadeo()
    escribir_temperatura()  
    sleep(INTERVALO)