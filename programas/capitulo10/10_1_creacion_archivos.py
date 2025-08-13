"""
MICROPYTHON EN PROYECTOS
Beatriz Padín / Adriana Dapena
Capítulo 10: Data logger
---------------------------------------
Se crea un archivo en el filesystem de la placa,
se escribe en él y se lee su contenido.
"""

import os

# Nombre del archivo
ARCHIVO = "prueba.txt"

# Se crea el achivo
print("--------------------------------------")
print("1. Creando el archivo '{}'...".format(ARCHIVO))
with open(ARCHIVO, "w") as archivo:
    archivo.write("Archivo de prueba")

# Se muestra el contenido del filesystem
print("--------------------------------------")
print("2. El archivo '{}' se ha creado en el filesystem.".format(ARCHIVO))
print(os.listdir())

# Se lee el achivo
print("--------------------------------------")
print("3. Contenido del archivo '{}':".format(ARCHIVO))
with open("prueba.txt", "r") as archivo:
    print(archivo.read())

# Se añade contenido al archivo
print("--------------------------------------")
print("4. Se añade contenido al archivo.")
with open("prueba.txt", "a") as archivo:
    archivo.write("\nPrueba 1")
    archivo.write("\nPrueba 2")
    archivo.write("\nPrueba 3")

# Se lee el achivo
print("--------------------------------------")
print("5. Nuevo contenido de '{}':".format(ARCHIVO))
with open("prueba.txt", "r") as archivo:
    print(archivo.read())