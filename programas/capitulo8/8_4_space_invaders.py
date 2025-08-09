"""
MICROPYTHON EN PROYECTOS
Beatriz Padín / Adriana Dapena
Capítulo 8: Música arcade
---------------------------------------
Se reproducen en bucle las notas mi-fa-fa#-sol
de Space Invaders.
"""

from machine import Pin, PWM
from time import sleep_ms

# Altavoz en GPIO18
# Se inicializa la señal PWM
# Se pone el altavoz en silencio
ALTAVOZ = PWM(Pin(18), duty_u16=0)

# Frecuencia de las notas musicales (Hz)
MI = 165
FA = 175
FA_S = 185
SOL = 196

# Duración de las notas y del silencio (ms)
DURACION_NOTA = 400
DURACION_SILENCIO = 200

# Nota musical
def nota(frecuencia, duracion):
    ALTAVOZ.duty_u16(32768)
    ALTAVOZ.freq(frecuencia)
    sleep_ms(duracion)

# Silencio  
def silencio(duracion):
    ALTAVOZ.duty_u16(0)
    sleep_ms(duracion)

while True:
    # Sol
    nota(SOL, DURACION_NOTA)
    silencio(DURACION_SILENCIO)
    # Fa sostenido
    nota(FA_S, DURACION_NOTA)
    silencio(DURACION_SILENCIO)
    # Fa
    nota(FA, DURACION_NOTA)
    silencio(DURACION_SILENCIO)
    # Mi
    nota(MI, DURACION_NOTA)
    silencio(DURACION_SILENCIO)