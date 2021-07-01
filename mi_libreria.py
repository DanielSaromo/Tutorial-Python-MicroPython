# libreria
from machine import ADC

class rpi_temperatura(object):
    def __init__ (self, vRef3v3=3.3):
        self.sensor_temp = ADC(4)
        self.factor_16 = vRef3v3 / (65535)
        
    def mideTemp(self):
        voltaje = self.sensor_temp.read_u16() * self.factor_16
        return 27 - (voltaje - 0.706)/0.001721