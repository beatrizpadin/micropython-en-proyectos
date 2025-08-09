"""
MICROPYTHON EN PROYECTOS
Beatriz Padín / Adriana Dapena
Capítulo 5: Señalización marítima
---------------------------------------
Se encienden dos ledes de manera intermitente.
El tiempo se controla usando un timer del
ESP32 o el Arduino Nano ESP32.
"""

from machine import Pin, Timer

# Led verde en el GPIO18, inicialmente encendido
LED_VERDE = Pin(18, Pin.OUT, value=1)

# Led rojo en el GPIO21, inicialmente apagado
LED_ROJO = Pin(21, Pin.OUT, value=0)

# Se usa el timer 0
TIMER = Timer(0)

# Intervalo de parpadeo (ms)
INTERVALO = 500

def parpadeo(t):
    # Los ledes parpadean alternativamente
    LED_VERDE.value(not LED_VERDE.value())
    LED_ROJO.value(not LED_ROJO.value())

# Se inicializa el timer
TIMER.init(period = INTERVALO,
           mode = Timer.PERIODIC,
           callback = parpadeo)