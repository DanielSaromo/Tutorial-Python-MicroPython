# sin libreria

from machine import ADC
from utime import sleep

class rpi_temperatura(object):
    def __init__ (self, vRef3v3=3.3):
        self.sensor_temp = ADC(4)
        self.factor_16 = vRef3v3 / (65535) # 16 bits de resolucion
        
    def mideTemp(self):
        voltaje = self.sensor_temp.read_u16() * self.factor_16
        return 27 - (voltaje - 0.706)/0.001721
        
def main():    
    obj_rpiTemp = rpi_temperatura() #Sensor interno de temperatura
    
    while True:        
        temperatura = obj_rpiTemp.mideTemp()
        print(temperatura)
        sleep(2)
        
    
if __name__ == '__main__':
    main()
