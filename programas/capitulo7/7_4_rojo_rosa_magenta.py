from machine import Pin, PWM
from time import sleep_ms

# Led RGB
# Rojo: GPIO 21, inicialmente encendido
# Verde: GPIO18, inicialmente apagado
# Azul: GPIO17, inicialmente apagado
LED_ROJO = PWM(Pin(21), freq=5000, duty_u16=65535)
LED_VERDE = PWM(Pin(18), freq=5000, duty_u16=0)
LED_AZUL = PWM(Pin(17), freq=5000, duty_u16=0)

# Se enciende el led azul progresivamente
for i in range(0, 65536, 100):
    LED_AZUL.duty_u16(i)
    sleep_ms(5)

# Se apaga el led
LED_ROJO.deinit()
LED_VERDE.deinit()
LED_AZUL.deinit()