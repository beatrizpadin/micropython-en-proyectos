"""
MICROPYTHON EN PROYECTOS
Beatriz Padín / Adriana Dapena
Capítulo 7: Rojo, verde y azul
---------------------------------------
Se enciende un led usando PWM.
"""

from machine import Pin, PWM
from time import sleep

# Led en el GPIO18
# Se activa la señal PWM
LED = PWM(Pin(18), freq=5000)

# Se enciende el led con una intensidad del 100%
LED.duty_u16(65535)
sleep(2)

# Se pone la intensidad al 50%
LED.duty_u16(32768)
sleep(2)

# Se apaga el led
LED.duty_u16(0)

# Se desactiva la señal PWM
LED.deinit()

