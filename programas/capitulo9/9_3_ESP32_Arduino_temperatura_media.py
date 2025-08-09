from machine import Pin, ADC
from time import sleep_ms

# Sensor de temperatura TMP36 conectado al GPIO14
TMP36 = ADC(Pin(14))

def voltaje_medio():
    i = 1
    suma = 0
    num = 20
    while i <= num:
        # ESP32, Arduino Nano ESP32
        voltaje = TMP36.read_uv()/1000000
        suma += voltaje
        i += 1
    media = suma/num
    return media    

while True:
    temperatura = (voltaje_medio() - 0.5)*100
    print(round(temperatura, 1))
    sleep_ms(500)