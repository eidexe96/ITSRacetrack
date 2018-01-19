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
    #identified = False
    activeCheckpoint = 1
    #teamid = teamid
    print("running")
    while identified == False:                                   #Loop solange kein Auto identifiziert ist
        print("startWhile")
        #qr.readQRCode()
        #teamid = 1 #qr.readQRCode()                      #Wenn der Scan funktioniert hat, wird die teamid und ein True-Flag zurückgegeben
        if teamid != 0:
            identified = True                                  #Initialisiere Startsequenz sobald ein Auto erkannt wurde
            print("identified")
            x = time.time()
            rslt.showResults(0, teamid, x)             #zeigt bisherige Ergebnisse des Teams an
            sound.playSound(-3)
            #sound.playSpeech(0, teamid)                          #erzählt infos zum Team
            print("sound played")
            fehlstart = lit.playStartSequence()                  #startet Ampel, Sounds und Fehlstartkontrolle
            print("light lit")
            if fehlstart:
                print("Fehlstart")
                break
            print("starttime")
            print(teamid)
            starttime = time.time()                                          #startet die Zeitmessung unabhängig davon, ob das Auto zu spät los fährt
    print("waiting for checkpoints")
    while identified == True:                                                   #Loop für Rennen, Messung etc.
        
        if cpl.checkpointReached(activeCheckpoint % 4):
            print("cpReached")
            cpl.saveTime(starttime, activeCheckpoint % 4)                       #speichert die LiveZeit vom aktuellen Checkpoint [0,1,2,3]
            #_thread.start_new_thread(lit.startLightExpress,())  #Ampel leuchtet, checkpointabhängig, läuft parallel
            #_thread.start_new_thread(sound.playSound,(activeCheckpoint))        #Spielt parallel den Sound, checkpointabhängig [1...8]
            #_thread.start_new_thread(sound.playSpeech,(activeCheckpoint, teamid)) #spricht (parallel),checkpointabhängig [1...8],teamid?
            rslt.showResults(activeCheckpoint, teamid, starttime)                #Zeigt Ergebnisse
            activeCheckpoint += 1
            print("nextCheckpoint:")
            print(activeCheckpoint)
        if activeCheckpoint == 8:
            _thread.start_new_thread(lit.startLightExpress,())
        if activeCheckpoint == 9:                                               #beendet das Rennen, speichert und zeigt Ergebnisse
            cpl.prepareDataForDB(teamid)                                        #rechnet einzelne Zeiten aus und schreibt diese in die DB
            rslt.showResults(9, teamid, starttime)
            rslt.showTime(starttime)
            lit.raceEnd()
            print("Rennen beendet")
            while 1:
                time.sleep(1)

                
try:
    print("Starting Programm")
    while 1:
        teamid=0
        teamid = qr.readQRCode()
        if teamid != 0:
            startProgramm(teamid)
except KeyboardInterrupt:
    print("Programm aborted")
    lit.raceEnd()
    pass