# LED on si aprueba

#Import Pin class from machine library to configure GPIO Pins.
from machine import Pin
#Import utime library to implement delay
import utime
#create an object of Pin class and set GPIO Parameters (GPIO Pin, Direction).
led_gpio25 = Pin(25, Pin.OUT)
#Create an infinite loop. This is similar to while(1) in C.

i = 0
sumaTotalNotas = 0
led_gpio25.value(0)

while True:
        i = i+1
        n = float(input("Ingrese el número # %s:  " % i))
        sumaTotalNotas += n
        
        prom = sumaTotalNotas / i
        
        print("El promedio es %f" % prom)
        
        if prom >=10.5:
            led_gpio25.value(1)
        else:
            led_gpio25.value(0)
        utime.sleep_ms(400)
        
        #MODO DE TOGGLEO
        #Toggle the status of LED.
        #led_gpio25.toggle()
        #sleep_ms function provides delay in milliseconds.
        #utime.sleep_ms(400)
