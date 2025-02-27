from machine import Pin, PWM
from neopixel import NeoPixel
import utime


servo = PWM(Pin(13), freq=50)    
pixels = NeoPixel(Pin(15), 16)
time = 0.5

rainbow = [
    (255, 255, 255), (114, 13, 0), (102, 25, 0), (90, 37, 0), (78, 49, 0), 
    (66, 61, 0), (54, 73, 0), (42, 85, 0), (30, 97, 0), (18, 109, 0), 
    (6, 121, 0), (0, 122, 5), (0, 110, 17), (0, 98, 29), (0, 86, 41), (42, 85, 0)
]


angulos = [
    0, 10, 20, 30, 40, 50, 60, 70, 80, 85, 90, 95, 100, 110, 120, 130, 
    140, 150, 160, 170, 180, 170, 160, 150, 140, 130, 120, 110, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0
]


def map(x):
    return int(((x - 0) * (125 - 25)) / (180 - 0) + 25) 


def angulo(a):
    m = map(a)
    servo.duty(m)
    utime.sleep(time)  


def rotar_neopixel_horario():
    rainbow.append(rainbow.pop(0))  
    for j in range(16):
        pixels[j] = rainbow[j]
    pixels.write()
    utime.sleep(time)


def rotar_neopixel_antihorario():
    rainbow.insert(0, rainbow.pop())  
    for j in range(16):
        pixels[j] = rainbow[j]
    pixels.write()
    utime.sleep(time)


def main():
    direccion = 1 

    while True:
        for i in range(len(angulos)):
            angulo_actual = angulos[i]
            angulo(angulo_actual)

            
            if i > 0:
                if angulos[i] > angulos[i - 1]:  
                    direccion = 1
                else:  
                    direccion = -1

        
            if direccion == 1:
                rotar_neopixel_horario()
            else:                
                rotar_neopixel_antihorario()

if _name_ == "_main_":
    main()