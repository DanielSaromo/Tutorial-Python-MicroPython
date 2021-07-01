# main que usa libreria
from utime import sleep
from mi_libreria import rpi_temperatura
        
def main():    
    obj_rpiTemp = rpi_temperatura() #Sensor interno de temperatura
    
    while True:        
        temperatura = obj_rpiTemp.mideTemp()
        print(temperatura)
        sleep(2)
        
    
if __name__ == '__main__':
    main()