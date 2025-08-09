from machine import Pin, ADC
from time import sleep

# Sensor de temperatura TMP36 conectado al GPIO14
TMP36 = ADC(Pin(14))

while True:
    # Lectura del voltaje en voltios
    # Raspberry Pi Pico
    lectura = TMP36.read_u16()
    voltaje = lectura*3.3/65535
    print(voltaje)
    sleep(1)