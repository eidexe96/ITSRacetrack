import time
print("imported time")
time.sleep(1)
import showResults as rslt
print("imported rslt")
time.sleep(1)
import readQRCode as qr
print("imported qr")
time.sleep(1)
import _thread
time.sleep(1)
import runServer as rs
print("imported threading")
time.sleep(1)
import checkpointLogic as cpl
print("imported checkpointlogic")
time.sleep(1)
import sound
print("imported sound")
time.sleep(1)
import light as lit
print("imported light")
time.sleep(1)

_thread.start_new_thread(rs.startServer,()) 
global identified
global activeCheckpoint
global teamid


def startProgramm(teamid):
    
    activeCheckpoint = 1
    print("running")
    x = time.time()
    rslt.showResults(0, teamid, x)             #zeigt bisherige Ergebnisse des Teams an
    sound.playSound(-3)
    sound.playSpeech(0, teamid)               #erzählt infos zum Team
    print("sound played")
    fehlstart = lit.playStartSequence()         #startet Ampel, Sounds und Fehlstartkontrolle
    print("light lit")
    
    if fehlstart:
        print("Fehlstart")
        
    print("starttime")
    print(teamid)
    starttime = time.time()                     #startet die Zeitmessung unabhängig davon, ob das Auto zu spät los fährt
    print("waiting for checkpoints")
    while teamid != 0:                                  #Loop für Rennen, Messung etc.
        if cpl.checkpointReached(activeCheckpoint % 4):
            print("cpReached")
            cpl.saveTime(starttime, activeCheckpoint % 4)
            #_thread.start_new_thread(lit.startLightExpress,()
            _thread.start_new_thread(sound.playSound,(activeCheckpoint, teamid, starttime))
            #_thread.start_new_thread(sound.playSpeech,(activeCheckpoint, teamid), )
            rslt.showResults(activeCheckpoint, teamid, starttime)        #Zeigt Ergebnisse
            activeCheckpoint += 1
            print("nextCheckpoint:")
            print(activeCheckpoint)
        if activeCheckpoint == 8:
            x=0 #lit.startLightExpress()
            #_thread.start_new_thread(lit.startLightExpress,())
        if activeCheckpoint == 9:                                         #beendet das Rennen, speichert und zeigt Ergebnisse
            cpl.prepareDataForDB(teamid)                                  #rechnet einzelne Zeiten aus und schreibt diese in die DB
            rslt.showResults(9, teamid, starttime)
            rslt.showTime(starttime)
            lit.raceEnd()
            print("Rennen beendet")
            time.sleep(6)
            sound.playSpeech(9, teamid, starttime)
            activeCheckpoint = 1
            teamid=0
            cpl.resetAll()
            #break
     
    
               

#qr.teamid = qrAlternative() #Falls der QR-Code Reader nicht geht, dies aktivieren und TeamID über Tastatur eingeben.

try:
    
    print("Starting Programm")
    teamid=0
    while 1:
        teamid = qr.readQRCode()
        if teamid != 0:
            startProgramm(teamid)
            print("sleep")
            time.sleep(8)
            sound.playSound(-4)
except KeyboardInterrupt:
    print("Programm aborted")
    lit.raceEnd()
    cpl.GPIO.cleanup()
    pass