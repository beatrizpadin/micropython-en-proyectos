"""
MICROPYTHON EN PROYECTOS
Beatriz Padín / Adriana Dapena
Capítulo 8: Música arcade
---------------------------------------
Se reproduce la melodía Korobéiniki del Tetris.
"""

from machine import Pin, PWM
from time import sleep_ms

# Altavoz en GPIO18
# Se inicializa la señal PWM
# Se pone el altavoz en silencio
ALTAVOZ = PWM(Pin(18), duty_u16=0)

# Frecuencia de las notas (Hz)
solS4 = 415
la4 = 440
laS4 = 466
si4 = 494
do5 = 523
doS5 = 554
re5 = 587
reS5 = 622
mi5 = 659
fa5 = 698
faS5 = 740
sol5 = 784
solS5 = 831
la5 = 880

# Duración de las notas en función del tempo
TEMPO = 144
pulso = 60000/TEMPO
blanca = int(2*pulso)
negra = int(1*pulso)
negra_punt = int(1.5*pulso)
corchea = int(0.5*pulso)

# Partitura: tono
korobeiniki_tono = [
    mi5, si4, do5, re5, do5, si4,   # Compás 1
    la4, la4, do5, mi5, re5, do5,   # Compás 2
    si4, do5, re5, mi5,             # Compás 3
    do5, la4, la4, la4, si4, do5,   # Compás 4
    re5, fa5, la5, sol5, fa5,       # Compás 5
    mi5, do5, mi5, re5, do5,        # Compás 6
    si4, si4, do5, re5, mi5,        # Compás 7
    do5, la4, la4, 0,               # Compás 8
    mi5, si4, do5, re5, do5, si4,   # Compás 1
    la4, la4, do5, mi5, re5, do5,   # Compás 2
    si4, do5, re5, mi5,             # Compás 3
    do5, la4, la4, la4, si4, do5,   # Compás 4
    re5, fa5, la5, sol5, fa5,       # Compás 5
    mi5, do5, mi5, re5, do5,        # Compás 6
    si4, si4, do5, re5, mi5,        # Compás 7
    do5, la4, la4, 0,               # Compás 8
    mi5, do5,                       # Compás 9
    re5, si4,                       # Compás 10
    do5, la4,                       # Compás 11
    solS4, si4, 0,                  # Compás 12
    mi5, do5,                       # Compás 13
    re5, si4,                       # Compás 14
    do5, mi5, la5,                  # Compás 15
    solS5, 0                        # Compás 16
    ]

# Partitura: duración
korobeiniki_duracion = [
    negra, corchea, corchea, negra, corchea, corchea,   # Compás 1
    negra, corchea, corchea, negra, corchea, corchea,   # Compás 2
    negra_punt, corchea, negra, negra,                  # Compás 3
    negra, negra, corchea, corchea, corchea, corchea,   # Compás 4
    negra_punt, corchea, negra, corchea, corchea,       # Compás 5
    negra_punt, corchea, negra, corchea, corchea,       # Compás 6
    negra, corchea, corchea, negra, negra,              # Compás 7
    negra, negra, negra, negra,                         # Compás 8
    negra, corchea, corchea, negra, corchea, corchea,   # Compás 1
    negra, corchea, corchea, negra, corchea, corchea,   # Compás 2 
    negra_punt, corchea, negra, negra,                  # Compás 3
    negra, negra, corchea, corchea, corchea, corchea,   # Compás 4 
    negra_punt, corchea, negra, corchea, corchea,       # Compás 5
    negra_punt, corchea, negra, corchea, corchea,       # Compás 6
    negra, corchea, corchea, negra, negra,              # Compás 7
    negra, negra, negra, negra,                         # Compás 8
    blanca, blanca,                                     # Compás 9
    blanca, blanca,                                     # Compás 10
    blanca, blanca,                                     # Compás 11
    blanca, negra, negra,                               # Compás 12
    blanca, blanca,                                     # Compás 13
    blanca, blanca,                                     # Compás 14
    negra, negra, blanca,                               # Compás 15
    blanca, blanca                                      # Compás 16
    ]

# Nota musical
def nota(frecuencia, tiempo):
    ALTAVOZ.duty_u16(32768)
    ALTAVOZ.freq(frecuencia)
    sleep_ms(tiempo)

# Silencio
def silencio(tiempo):
    ALTAVOZ.duty_u16(0)
    sleep_ms(tiempo)

# Se interpreta la melodía
for i in range(len(korobeiniki_tono)):
    if korobeiniki_tono[i] == 0:
        silencio(korobeiniki_duracion[i])
    else:
        nota(korobeiniki_tono[i], korobeiniki_duracion[i])
        silencio(10)