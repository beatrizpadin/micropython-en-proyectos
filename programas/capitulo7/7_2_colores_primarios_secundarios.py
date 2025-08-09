from machine import Pin, PWM
from time import sleep

# Led RGB inicialmente apagado
# Rojo: GPIO 21
# Verde: GPIO18
# Azul: GPIO17
LED_ROJO = PWM(Pin(21), freq=5000, duty_u16=0)
LED_VERDE = PWM(Pin(18), freq=5000, duty_u16=0)
LED_AZUL = PWM(Pin(17), freq=5000, duty_u16=0)

# Rojo
LED_ROJO.duty_u16(65535)
LED_VERDE.duty_u16(0)
LED_AZUL.duty_u16(0)
sleep(1)

# Verde
LED_ROJO.duty_u16(0)
LED_VERDE.duty_u16(65535)
LED_AZUL.duty_u16(0)
sleep(1)

# Azul
LED_ROJO.duty_u16(0)
LED_VERDE.duty_u16(0)
LED_AZUL.duty_u16(65535)
sleep(1)

# Amarillo
LED_ROJO.duty_u16(65535)
LED_VERDE.duty_u16(65535)
LED_AZUL.duty_u16(0)
sleep(1)

# Cian
LED_ROJO.duty_u16(0)
LED_VERDE.duty_u16(65535)
LED_AZUL.duty_u16(65535)
sleep(1)

# Magenta
LED_ROJO.duty_u16(65535)
LED_VERDE.duty_u16(0)
LED_AZUL.duty_u16(65535)
sleep(1)

# Se apaga el led
LED_ROJO.deinit()
LED_VERDE.deinit()
LED_AZUL.deinit()


