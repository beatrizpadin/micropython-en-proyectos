from machine import Pin, PWM

# Led RGB inicialmente apagado
# Rojo: GPIO 21
# Verde: GPIO18
# Azul: GPIO17
LED_ROJO = PWM(Pin(21), freq=5000, duty_u16=0)
LED_VERDE = PWM(Pin(18), freq=5000, duty_u16=0)
LED_AZUL = PWM(Pin(17), freq=5000, duty_u16=0)

# Azul turquesa: 6% rojo, 87% verde, 69% azul
r = 6
g = 87
b = 69

# Se enciende el led
LED_ROJO.duty_u16(int(r/100*65535))
LED_VERDE.duty_u16(int(g/100*65535))
LED_AZUL.duty_u16(int(b/100*65535))