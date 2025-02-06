import time
from Freenove_DHT import DHT      

DHTPin = 17

def loop():
    dht = DHT(DHTPin)
    time.sleep(1) 
    counts = 0 
    while(True):
        counts += 1
        print("Measurement counts: ", counts)
        for i in range(0,15):            
            chk = dht.readDHT11()
            if (chk == 0):
                print("DHT11,OK!")
                break
            time.sleep(0.1)
           
        print("Humidity : %.2f, \t Temperature : %.2f \n"%(dht.getHumidity(),dht.getTemperature()))
        time.sleep(2)   
        
if __name__ == '__main__':
    print ('Program is starting ... ')
    try:
        loop()
    except KeyboardInterrupt:
        pass
        exit()   