
import smbus
from time import sleep, strftime
from datetime import datetime
from LCD1602 import CharLCD1602

lcd1602 = CharLCD1602()    
def get_cpu_temp(): 
    tmp = open('/sys/class/thermal/thermal_zone0/temp')
    cpu = tmp.read()
    tmp.close()
    return '{:.2f}'.format( float(cpu)/1000 ) + ' C '
 
def get_time_now():
    return datetime.now().strftime('    %H:%M:%S')
    
def loop():
    lcd1602.init_lcd()
    count = 0
    while(True):
        lcd1602.clear()
        lcd1602.write(0, 0, 'CPU: ' + get_cpu_temp() )
        lcd1602.write(0, 1, get_time_now() )
        sleep(1)
def destroy():
    lcd1602.clear()
if __name__ == '__main__':
    print ('Program is starting ... ')
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
    