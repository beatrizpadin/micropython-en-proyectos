"""
MICROPYTHON EN PROYECTOS
Beatriz Padín / Adriana Dapena
Capítulo 8: Música arcade
---------------------------------------
Se reproducen las notas mi-fa-fa#-sol de Space Invaders
cada vez más rápido. Cuando se alcanza el tempo máximo
se vuelve a empezar.
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

# Tempo inicial (ppm)
TEMPO_0 = 80

# Tempo máximo (ppm)
TEMPO_MAX = 300

# Incremento en el tempo (ppm)
INCREMENTO = 10

# Se inicializa la variable tempo (bpm)
tempo = TEMPO_0


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
    

def melodia(t):
    """
    Interpreta la melodía con un tempo determinado.
    """
    # Duraciones en función del tempo
    pulso = 60000/t
    duracion_nota = int(2/3*pulso)
    duracion_silencio = int(1/3*pulso)
    
    # Se reproducen las notas
    nota(SOL, duracion_nota)
    silencio(duracion_silencio)
    nota(FA_S, duracion_nota)
    silencio(duracion_silencio)
    nota(FA, duracion_nota)
    silencio(duracion_silencio)
    nota(MI, duracion_nota)
    silencio(duracion_silencio)


while True:
    while tempo <= TEMPO_MAX:
        # Se interpreta la melodía
        melodia(tempo)
        # El tempo se incrementa
        tempo += INCREMENTO 
    # Se vuelve al tempo inicial
    tempo = TEMPO_0
    # Se espera 1 s antes de volver a empezar
    sleep_ms(1000)