from gpiozero import InputDevice, OutputDevice
import time
class Key(object):
    NO_KEY = '\0'
    IDLE = 0
    PRESSED = 1
    HOLD = 2
    RELEASED = 3
    OPEN = 0
    CLOSED =1
    def __init__(self):
        self.kchar = self.NO_KEY
        self.kstate = self.IDLE
        self.kcode = -1
        self.stateChanged = False

class Keypad(object):
    NULL = '\0'
    LIST_MAX = 10
    MAPSIZE = 10
    bitMap = [0]*MAPSIZE
    key = [Key()]*LIST_MAX
    holdTime = 500
    holdTimer = 0
    startTime = 0
    def __init__(self,usrKeyMap,row_Pins,col_Pins,num_Rows,num_Cols):
        self.rowPins = row_Pins
        self.colPins = col_Pins
        self.numRows = num_Rows
        self.numCols = num_Cols
        
        self.keymap = usrKeyMap
        self.setDebounceTime(10)
    def getKey(self):
        single_key = True
        if(self.getKeys() and self.key[0].stateChanged and (self.key[0].kstate == self.key[0].PRESSED)):
            return self.key[0].kchar
        single_key = False
        return self.key[0].NO_KEY
    def getKeys(self):
        keyActivity = False
        if((time.time() - self.startTime) > self.debounceTime*0.001):
            self.scanKeys()
            keyActivity = self.updateList()
            self.startTime = time.time()
        return keyActivity
    def scanKeys(self):
        inputs = list(map(lambda pin: InputDevice(pin, pull_up=True), self.rowPins))
        for pin_c in self.colPins:
            outputs = OutputDevice(pin_c)
            outputs.off()
            i=0
            for r in self.rowPins:
                self.bitMap[self.rowPins.index(r)] = self.bitWrite(self.bitMap[self.rowPins.index(r)],self.colPins.index(pin_c), inputs[i].value)
                i =i+1
            outputs.on()
            outputs.close()
            outputs = InputDevice(pin_c,pull_up=True)
    def updateList(self):
        anyActivity = False
        kk = Key()
        for i in range(self.LIST_MAX):
            if(self.key[i].kstate == kk.IDLE):
                self.key[i].kchar = kk.NO_KEY
                self.key[i].kcode = -1
                self.key[i].stateChanged = False
        for r in range(self.numRows):
            for c in range(self.numCols):
                button = self.bitRead(self.bitMap[r],c)
                keyChar = self.keymap[r * self.numCols +c]
                keyCode = r * self.numCols +c
                idx = self.findInList(keyCode)
                if(idx > -1):
                    self.nextKeyState(idx,button)
                if((idx == -1) and button):
                    for i in range(self.LIST_MAX):
                        if(self.key[i].kchar == kk.NO_KEY):
                            self.key[i].kchar = keyChar
                            self.key[i].kcode = keyCode
                            self.key[i].kstate = kk.IDLE
                            self.nextKeyState(i,button)
                            break
        for i in range(self.LIST_MAX):
            if(self.key[i].stateChanged):
                anyActivity = True
        return anyActivity      
    def nextKeyState(self,idx, button):
        self.key[idx].stateChanged = False
        kk = Key()
        if(self.key[idx].kstate == kk.IDLE):
            if(button == kk.CLOSED):
                self.transitionTo(idx,kk.PRESSED)
                self.holdTimer = time.time()    #Get ready for next HOLD state.
        elif(self.key[idx].kstate == kk.PRESSED):
            if((time.time() - self.holdTimer) > self.holdTime*0.001):   #Waiting for a key HOLD...  
                self.transitionTo(idx,kk.HOLD)
            elif(button == kk.OPEN):        # or for a key to be RELEASED.
                self.transitionTo(idx,kk.RELEASED)
        elif(self.key[idx].kstate == kk.HOLD):
            if(button == kk.OPEN):
                self.transitionTo(idx,kk.RELEASED)
        elif(self.key[idx].kstate == kk.RELEASED):
            self.transitionTo(idx,kk.IDLE)
            
    def transitionTo(self,idx,nextState):
        self.key[idx].kstate = nextState
        self.key[idx].stateChanged = True
    #Search by code for a key in the list of active keys.
    #Returns -1 if not found or the index into the list of active keys.
    def findInList(self,keyCode):
        for i in range(self.LIST_MAX):
            if(self.key[i].kcode == keyCode):
                return i
        return -1
    #set Debounce Time, The default is 50ms                 
    def setDebounceTime(self,ms):
        self.debounceTime = ms
    #set HoldTime,The default is 500ms
    def setHoldTime(self,ms):
        self.holdTime = ms
    #   
    def isPressed(keyChar):
        for i in range(self.LIST_MAX):
            if(self.key[i].kchar == keyChar):
                if(self.key[i].kstate == self.self.key[i].PRESSED and self.key[i].stateChanged):
                    return True
        return False
    #           
    def waitForKey():
        kk = Key()
        waitKey = kk.NO_KEY
        while(waitKey == kk.NO_KEY):
            waitKey = getKey()
        return waitKey
    
    def getState():
        return self.key[0].kstate
    #   
    def keyStateChanged():
        return self.key[0].stateChanged
    
    def bitWrite(self,x,n,b):
        if(b):
            x |= (1<<n)
        else:
            x &=(~(1<<n))
        return x
    def bitRead(self,x,n):
        if((x>>n)&1 == 1):
            return True
        else:
            return False

ROWS = 4
COLS = 4
keys =  [   '1','2','3','A',
            '4','5','6','B',
            '7','8','9','C',
            '*','0','#','D'     ]
rowsPins = [18, 23, 24, 25]
colsPins = [10, 22, 27, 17]    

def loop():
    keypad = Keypad(keys,rowsPins,colsPins,ROWS,COLS)
    keypad.setDebounceTime(50)
    while(True):
        key = keypad.getKey()
        if(key != keypad.NULL):
            print ("You Pressed Key : %c "%(key) )
        
if __name__ == '__main__': 
    print ("Program is starting ... ")
    try:
        loop()
    except KeyboardInterrupt:
        print("Ending program")