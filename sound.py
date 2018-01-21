from subprocess import call
from random import randint
import math
global minu
global sec
global text
global sound
import light as lit
import time


#speech synthesis functions

def time_convert(t):
    min = math.floor(t/60)
    sec = t%60

def playSpeech(check, teamID):
    
    if check == 0 or check == 2 or check == 3 or check == 5 or check == 6 or check == 7:
        z = randint(1,3)
        if z == 1:
            text = "Beispiel 1"
        elif z == 2:
            text = "Beispiel 2"
        elif z == 3:
            text = "Beispiel 3"
        elif z > 5:
            text = ""
            
    elif check == 4:
        z = randint(1,3)
        if z == 1:
            text = "So schlecht war Tiem 1 noch nie"
        elif z == 2:
            text = "So schlecht war Tiem 1 noch nie"
        elif z == 3:
            text = "So schlecht war Tiem 1 noch nie"
            
    elif check == 8:
        z = randint(1,3)
        if z == 1:
            text = "Beispiel 1"
        elif z == 2:
            text = "Beispiel 2"
        elif z == 3:
            text = "Beispiel 3"
    
    call(["espeak", "-vmb-de5", text, "2>/dev/null"])

def s_speech(var2):
    call(["pico2wave", "-lang=de-DE", "-wave=/home/pi/work/sound/test.wav", var2])
    call(["aplay", "/home/pi/work/sound/test.wav"])
    call(["rm", "/home/pi/work/sound/test.wav"])
    
    
    
#sound function

def playSound(check, teamid, starttime):
    if check == -4
        sound = "boing.wav"
        
    elif check == -3:
        sound = "scan.wav" 
        
    elif check == -2:
        sound = "start.wav"
        
    elif check == -1:
        sound = "beep_1.wav"
        
    elif check == 0:
        sound = "beep_2.wav"
        
    elif check == 1 or check == 2 or check == 3 or check == 5 or check == 6:
        sound = "checkpoint.wav"
        
    elif check == 7:
        sound = "checkpoint.wav"
        lit.allBlue()
        lit.strip.show()
        
    elif check == 4:
        sound = "2nd_lap.wav"
        
    elif check == 8:
        4th_best_gesamt = readData(teamid)[8]
        time_now = time.time() - starttime
        if time_now < 4th_best_gesamt:
            sound = "end_good.wav"
        else:
            sound = "end_bad.wav"

    
    call(["aplay", "/home/pi/work/its/ITSRacetrack/sounds/"+sound])
    
    if check == 8:
        time.sleep(8)
        playSpeech(check, teamid, time_now)
        
    
    
#playSound(-3)
#playSpeech(4,3)