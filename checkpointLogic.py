import time

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(4, GPIO.RISING)

class checkpt:
    'Base class for all Checkpoints'
    count = 0
    allCpts = []
    
    def __init__(self, nr, time1=0, time2=0, check1 = False, check2 = False):
        self.nr = nr
        self.time1 = time1
        self.time2 = time2
        self.check1 = check1
        self.check2 = check2
        checkpt.count +=1
        checkpt.allCpts.append(self)
    
    def resetCpt(self):
        self.time1 = 0
        self.time2 = 0
        self.check1 = False
        self.check2 = False
    

    
    def saveTime(self, starttime):
        if (self.starttime != 0):
            if (self.check1 == False):
                self.time1 = time.clock() - self.starttime
                self.check1 = True
            elif (self.check2 == False):
                self.time2 = time.clock() - self.starttime
                self.check2 = True

cp0 = checkpt(0)
cp1 = checkpt(1)
cp2 = checkpt(2)
cp3 = checkpt(3)



def resetAll(all):
    for item in all:
        item.resetCpt()

        
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
        return GPIO.input(0)
    elif (checkNr == 1):
        return GPIO.input(1)
    elif (checkNr == 2):
        return GPIO.input(2)
    elif (checkNr == 3):
        return GPIO.input(3)


    
def prepareDataForDB(teamid):
    time101 = cp1.time1
    time201 = cp1.time2 - cp0.time1
    if (time101<=time201):            #beste Zeit für Abschnitt 1 bestimmt
        time01 = time101
    else
        time01 = time201
    
    time112 = cp2.time1 - cp1.time1
    time212 = cp2.time2 - cp1.time2
    if (time112<=time212):            #beste Zeit für Abschnitt 2 bestimmt
        time12 time112
    else
        time12 time212
    
    time123 = cp3.time1 - cp2.time1
    time212 = cp3.time2 - cp2.time2
    if (time123<=time223):            #beste Zeit für Abschnitt 3 bestimmt
        time23 time123
    else
        time23 time223
        
    time130 = cp0.time1 - cp3.time1
    time230 = cp0.time2 - cp3.time2
    if (time130<=time230):            #beste Zeit für Abschnitt 4 bestimmt
        time30 time130
    else
        time30 time230        
        
    round1 = roundSum1(checkpt.allCpts)
    round2 = roundSum2(checkpt.allCpts)
    if (round1 <= round2):
        bestround = round1            #beste Rundenzeit bestimmt
    else
        bestround = round2
    
    totalTime = round1 + round2
    
    writetoDB(teamid, totalTime, bestround, time01, time12, time23, time30, 0) #0 Platzhalter, falls noch benötigt
    