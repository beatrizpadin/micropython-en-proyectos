from machine import Pin, ADC
from time import sleep

# Sensor de temperatura TMP36 conectado al GPIO14
TMP36 = ADC(Pin(14))

while True:
    # Temperatura en grados centígrados
    # ESP32, Arduino Nano ESP32
    voltaje = TMP36.read_uv()/1000000
    temperatura = (voltaje - 0.5)*100
    print(round(temperatura, 1))
    sleep(1)