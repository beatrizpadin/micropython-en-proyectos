"""
MICROPYTHON EN PROYECTOS
Beatriz Padín / Adriana Dapena
Capítulo 8: Música arcade
---------------------------------------
Se interpretan las notas do-ro-mi,
separadas por un breve silencio.
"""

from machine import Pin, PWM
from time import sleep_ms

# Altavoz en GPIO18
# Se inicializa la señal PWM
ALTAVOZ = PWM(Pin(18))

# Se pone el altavoz en silencio
ALTAVOZ.duty_u16(0)

# Frecuencia de las notas musicales (Hz)
DO = 262
RE = 294
MI = 330

# Duración de las notas y del silencio (ms)
DURACION_NOTA = 250
DURACION_SILENCIO = 250


def nota(frecuencia, duracion):
    """
    Interpreta una nota musical dada la frecuencia y la duración.
    """
    ALTAVOZ.duty_u16(32768)
    ALTAVOZ.freq(frecuencia)
    sleep_ms(duracion)


def silencio(duracion):
    """
    Interpreta un silencio de una duración determinada.
    """
    ALTAVOZ.duty_u16(0)
    sleep_ms(duracion)


def apagado():
    """
    Desactiva la señal PWM.
    """
    ALTAVOZ.deinit()


# Do
nota(DO, DURACION_NOTA)
silencio(DURACION_SILENCIO)

# Re
nota(RE, DURACION_NOTA)
silencio(DURACION_SILENCIO)

# Mi
nota(MI, DURACION_NOTA)
silencio(DURACION_SILENCIO)

# Se desactiva el altavoz
apagado()