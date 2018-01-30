import time
import writeToDb as wtdb
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

global time01
global time12
global time23
global time30
global bestround
global totalTime




class checkpt:
    'Base class for all Checkpoints'
    count = 0
    allCpts = []
    
    def __init__(self, nr, outputPin, inputPin, time1=0, time2=0, check1 = False, check2 = False, round1 = 0, round2 = 0):
        self.nr = nr
        self.time1 = time1
        self.time2 = time2
        self.check1 = check1
        self.check2 = check2
        self.outputPin = outputPin
        self.inputPin = inputPin
        checkpt.count +=1
        checkpt.allCpts.append(self)
        
        
    def assignPins(self):
        i = self.inputPin
        o = self.outputPin
        GPIO.setup(o, GPIO.OUT)
        GPIO.output(o, 1)
        GPIO.setup(i, GPIO.IN)
        GPIO.input(i)
    
    def resetCpt(self):
        self.time1 = 0
        self.time2 = 0
        self.check1 = False
        self.check2 = False
    

    
    def savePartTime(self, starttime):
        if (starttime != 0):
            if (self.check1 == False):
                self.time1 = time.time() - starttime
                self.round1 = time.time() - starttime
                self.check1 = True
                print("time1 set")
            elif (self.check2 == False):
                self.time2 = time.time() - starttime
                self.round2 = time.time() - starttime
                self.check2 = True
                print("time2 set")

                
                
cp0 = checkpt(0, 4, 17)
cp1 = checkpt(1, 5, 6)
cp2 = checkpt(2, 23, 24)
cp3 = checkpt(3, 16, 20)
cp0.assignPins()
cp1.assignPins()
cp2.assignPins()
cp3.assignPins()



def saveTime(starttime, checkNr):
    if (checkNr == 0):
        cp0.savePartTime(starttime)
    elif (checkNr == 1):
        cp1.savePartTime(starttime)
    elif (checkNr == 2):
        cp2.savePartTime(starttime)
    elif (checkNr == 3):
        cp3.savePartTime(starttime)
    print(checkNr)

def resetAll():
    cp0.resetCpt()
    cp1.resetCpt()
    cp2.resetCpt()
    cp3.resetCpt()
    
        
def resetGPIOs():
    GPIO.cleanup()
        
def roundSum1(all):
    round1 = 0
    for item in all:
        round1 += item.time1
    return round1

def roundSum2(all):
    round2 = 0
    for item in all:
        round2 += item.time2
    return round2


        
def checkpointReached(checkNr):
    if (checkNr == 0):
        return GPIO.input(cp0.inputPin)
    elif (checkNr == 1):
        return GPIO.input(cp1.inputPin)
    elif (checkNr == 2):
        return GPIO.input(cp2.inputPin)
    elif (checkNr == 3):
        return GPIO.input(cp3.inputPin)


    
def prepareDataForDB(teamid):
    totalTime = 2
    time101 = cp1.time1
    time201 = cp1.time2 - cp0.time1
    if (time101<=time201):            #determine best time for part 1
        time01 = time101
    else:
        time01 = time201
    
    time112 = cp2.time1 - cp1.time1
    time212 = cp2.time2 - cp1.time2
    if (time112<=time212):            #determine best time for part 2
        time12 = time112
    else:
        time12 = time212
    
    time123 = cp3.time1 - cp2.time1
    time223 = cp3.time2 - cp2.time2
    if (time123<=time223):            #determine best time for part 3
        time23 = time123
    else:
        time23 = time223
        
    time130 = cp0.time1 - cp3.time1
    time230 = cp0.time2 - cp3.time2
    if (time130<=time230):            #determine best time for part 4
        time30 = time130
    else:
        time30 = time230        
    
    round1 = cp0.round1
    round2 = cp0.round2-cp0.round1
    if (round1 <= round2):
        bestround = round1            #determine best lap time
    else:
        bestround = round2
    
    totalTime = round1 + round2
    
    
    #teamid, totalTime, bestround, time01, time12, time23, time30, "ijöööö") #0 place holder if needed
    wtdb.writeToDb(teamid, round(totalTime,0), round(bestround,0), round(time01,0), round(time12,0), round(time23,0), round(time30,0), "ijöööö")
