"""
MICROPYTHON EN PROYECTOS
Beatriz Padín / Adriana Dapena
Capítulo 4: Los módulos integrados
---------------------------------------
Se programa una cuenta atrás para ilustrar
cómo medir tiempos con precisión.
"""

from time import sleep

# Número inicial en la cuenta atrás
i = 5

while i >= 0:
    print(i)
    sleep(1)
    i -= 1