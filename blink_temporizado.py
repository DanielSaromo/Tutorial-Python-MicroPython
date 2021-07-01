# Blink

#Import Pin class from machine library to configure GPIO Pins.
from machine import Pin
#Import utime library to implement delay
import utime
#create an object of Pin class and set GPIO Parameters (GPIO Pin, Direction).
led_gpio25 = Pin(25, Pin.OUT)
#Create an infinite loop. This is similar to while(1) in C.
while True:
    for i in range(10):
        #Set value to 1 to turn ON LED.
        led_gpio25.value(1)
        #sleep_ms function provides delay in milliseconds.
        utime.sleep_ms(25*i+10+int(i*i/10))
        #Set value to 0 to turn OFF LED.
        led_gpio25.value(0)
        #Provide another 100ms delay to see the LED Blinking.
        utime.sleep_ms(50*i)
        
        #MODO DE TOGGLEO
        #Toggle the status of LED.
        #led_gpio25.toggle()
        #sleep_ms function provides delay in milliseconds.
        #utime.sleep_ms(400)
