from subprocess import call
from random import randint
global text
#speech synthesis functions

def playSpeech(check, teamID):
    
    if check == 1 or check == 2 or check == 3 or check == 5 or check == 6 or check == 7:
        z = randint(1,10)
        if z == 1:
            text = "Beispiel 1"
        elif z == 2:
            text = "Beispiel 2"
        elif z == 3:
            text = "Beispiel 3"
        elif z > 5:
            text = ""
            
    elif check == 4:
        z = randint(1,5)
        if z == 1:
            text = "Beispiel 1"
        elif z == 2:
            text = "Beispiel 2"
        elif z == 3:
            text = "Beispiel 3"
            
    elif check == 8:
        z = randint(1,5)
        if z == 1:
            text = "Beispiel 1"
        elif z == 2:
            text = "Beispiel 2"
        elif z == 3:
            text = "Beispiel 3"
    
    call(["espeak", "-vmb-de4", text, "2>/dev/null"])

def s_speech(var2):
    call(["pico2wave", "-lang=de-DE", "-wave=/home/pi/work/sound/test.wav", var2])
    call(["aplay", "/home/pi/work/sound/test.wav"])
    call(["rm", "/home/pi/work/sound/test.wav"])
    
    
    
#sound function

def playSound(check):
    
    if check == -3:
        sound = "scan.wav" 
    elif check == -2:
        sound = "start.wav"
    elif check == -1:
        sound = "beep_1.wav"
    elif check == 0:
        sound = "beep_2.wav"
    elif check == 2 or check == 3 or check == 4 or check == 6 or check == 7 or check == 8:
        sound = "checkpoint.wav"
    elif check == 5:
        sound = "2nd_lap.wav"
    elif check == 9:
        sound = "end_good.wav"
    
    call(["aplay", "/home/pi/its/ITSRacetrack/sounds/"+sound])
        
    
    
    


