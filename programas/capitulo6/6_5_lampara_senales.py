"""
MICROPYTHON EN PROYECTOS
Beatriz Padín / Adriana Dapena
Capítulo 6: Lámpara de señales
---------------------------------------
Pulsador 1: Luz verde fija. Autorizado para aterrizar.
Pulsador 2: Luz roja intermitente. Peligro, no aterrice.
Pulsador 3: Luz alterna roja y verde. Extreme la precaución.
"""

from machine import Pin
from time import sleep_ms

# Pulsador 1 en GPIO17: aterrice
# Pulsador 2 en GPIO14: peligro
# Pulsador 3 en GPIO13: precaución 
PULSADOR_1 = Pin(17, Pin.IN, Pin.PULL_UP)
PULSADOR_2 = Pin(14, Pin.IN, Pin.PULL_UP)
PULSADOR_3 = Pin(13, Pin.IN, Pin.PULL_UP)

# Led verde en GPIO18
# Led rojo en GPIO21
LED_VERDE = Pin(18, Pin.OUT, value=0)
LED_ROJO = Pin(21, Pin.OUT, value=0)

# Tiempo entre destellos (en ms)
INTERVALO = 500


def apagado():
    """
    Ambos ledes apagados
    """
    LED_VERDE.value(0)
    LED_ROJO.value(0)


def aterrice():
    """
    Led verde fijo
    """
    LED_VERDE.value(1)


def peligro():
    """
    Led rojo intermitente
    """
    LED_ROJO.value(not LED_ROJO.value())
    sleep_ms(INTERVALO)


def precaucion():
    """
    Led verde y rojo alternos
    """
    LED_VERDE.value(1)
    LED_ROJO.value(0)
    sleep_ms(INTERVALO)
    LED_VERDE.value(0)
    LED_ROJO.value(1)
    sleep_ms(INTERVALO)


while True:
    if PULSADOR_1.value() == 1 and PULSADOR_2.value() == 1 and PULSADOR_3.value() == 1:
        apagado()
    elif PULSADOR_1.value() == 0:
        aterrice()
    elif PULSADOR_2.value() == 0:
        peligro()
    elif PULSADOR_3.value() == 0:
        precaucion()