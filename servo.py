#Autores: Andrés Galvis, Keppler Sánchez y Daniel Viafara.

from machine import Pin, PWM
from neopixel import NeoPixel
import utime

# Configuración del servo en ESP32 (GPIO 13)
servo = PWM(Pin(13), freq=50)

# Configuración de la tira Neopixel (GPIO 15, 16 LEDs)
num_leds = 16
pixels = NeoPixel(Pin(15), num_leds)

# Gradientes de colores
blue_gradient = [(0, 0, i * 16) for i in range(num_leds)]
red_gradient = [(i * 16, 0, 0) for i in range(num_leds)]

# Función para mapear valores de ángulo a "duty cycle" del servo
def map_value(x, in_min, in_max, out_min, out_max):
    return round((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

# Función para mover el servo a un ángulo específico
def mover_servo(angulo):
    pwm_value = map_value(angulo, 0, 180, 40, 115)  
    servo.duty(pwm_value)

# Función para actualizar el LED en Neopixel
def actualizar_neopixel(angulo, direccion):
    posicion_led = round((angulo / 180) * (num_leds - 1))
    gradient = blue_gradient if direccion == 1 else red_gradient

    for i in range(num_leds):
        pixels[i] = gradient[i]
    
    pixels[posicion_led] = (255, 255, 255)  # LED blanco en la posición actual
    pixels.write()

# Función principal
def main():
    angulo = 0
    direccion = 1  # 1: aumentando, -1: disminuyendo

    while True:
        mover_servo(angulo)
        actualizar_neopixel(angulo, direccion)

        if angulo >= 180:
            direccion = -1
        elif angulo <= 0:
            direccion = 1

        angulo += direccion * 5  # Incremento en pasos de 5°
        utime.sleep_ms(100)

if __name__ == "__main__":
    main()
