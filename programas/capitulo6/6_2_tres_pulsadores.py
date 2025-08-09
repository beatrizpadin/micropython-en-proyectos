from machine import Pin
from time import sleep_ms

# Pulsador 1 en el GPIO17
PULSADOR_1 = Pin(17, Pin.IN, Pin.PULL_UP)

# Pulsador 2 en el GPIO14
PULSADOR_2 = Pin(14, Pin.IN, Pin.PULL_UP)

# Pulsador 3 en el GPIO13
PULSADOR_3 = Pin(13, Pin.IN, Pin.PULL_UP)

while True:
    if PULSADOR_1.value() == 0:
        print("Se está pulsando el botón 1")
    elif PULSADOR_2.value() == 0:
        print("Se está pulsando el botón 2")
    elif PULSADOR_3.value() == 0:
        print("Se está pulsando el botón 3")
    else:
        print("No se está pulsando ningún botón")
    sleep_ms(200)