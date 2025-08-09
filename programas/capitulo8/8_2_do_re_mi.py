"""
MICROPYTHON EN PROYECTOS
Beatriz Padín / Adriana Dapena
Capítulo 8: Música arcade
---------------------------------------
Se interpretan las notas do-ro-mi.
"""

from machine import Pin, PWM
from time import sleep_ms

# Altavoz en GPIO18
# Se inicializa la señal PWM
ALTAVOZ = PWM(Pin(18), duty_u16=32768)

# Frecuencia de las notas musicales (Hz)
DO = 262
RE = 294
MI = 330

# Duración de las notas (ms)
DURACION = 500

# Do
ALTAVOZ.freq(DO)
sleep_ms(DURACION)

# Re
ALTAVOZ.freq(RE)
sleep_ms(DURACION)

# Mi
ALTAVOZ.freq(MI)
sleep_ms(DURACION)

# Se desactiva la señal
ALTAVOZ.deinit()

