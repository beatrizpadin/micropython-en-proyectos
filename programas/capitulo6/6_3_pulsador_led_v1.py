from machine import Pin

# Pulsador en el GPIO17
PULSADOR = Pin(17, Pin.IN, Pin.PULL_UP)

# Led en el GPIO18
LED = Pin(18, Pin.OUT)

while True:
    # Botón pulsado
    if PULSADOR.value() == 0:
        # Se enciende el led
        LED.value(1)
        
    # Botón no pulsado
    else:
        # Se apaga el led
        LED.value(0)