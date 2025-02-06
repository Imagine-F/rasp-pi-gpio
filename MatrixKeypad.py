import Keypad 
ROWS = 4
COLS = 4 
keys =  [   '1','2','3','A',
            '4','5','6','B',
            '7','8','9','C',
            '*','0','#','D'     ]
rowsPins = [18, 23, 24, 25]
colsPins = [10, 22, 27, 17]
def loop():
    keypad = Keypad.Keypad(keys,rowsPins,colsPins,ROWS,COLS)
    keypad.setDebounceTime(50)
    while(True):
        key = keypad.getKey()
        if(key != keypad.NULL):
            print ("You Pressed Key : %c "%(key))
            
if __name__ == '__main__':
    print ("Program is starting ... ")
    try:
        loop()
    except KeyboardInterrupt:
        print("Ending program")