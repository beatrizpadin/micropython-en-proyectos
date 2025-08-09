"""
MICROPYTHON EN PROYECTOS
Beatriz Padín / Adriana Dapena
Capítulo 4: Los módulos integrados
---------------------------------------
Se programa un cronómetro para ilustrar
cómo medir tiempos con precisión.
"""

from time import ticks_ms, ticks_diff

print("--------------------------------------")
print("Haz clic en la consola para activarla.")
print("START: Pulsa la tecla Intro para iniciar el cronómetro.")
print("STOP: Vuelve a pulsar Intro para pararlo.")
print("--------------------------------------")

# Inicio
input()
inicio = ticks_ms()
print("Instante inicial (ms):", inicio)

# Fin
input()
fin = ticks_ms()
print("Instante final (ms):", fin)

# Tiempo
tiempo = ticks_diff(fin, inicio)
print("\nTiempo (s):", tiempo/1000)