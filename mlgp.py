import time
import showResults as rslt
print("imported time")
import readQRCode as qr
print("imported qr")
import _thread
import runServer as rs
print("imported threading")
import checkpointLogic as cpl
print("imported checkpointlogic")
#import sound
print("imported sound")
import light as lit
print("imported light")

_thread.start_new_thread(rs.startServer,())
global identified
global activeCheckpoint
global teamid

def startProgramm():
    identified = False
    activeCheckpoint = 1
    teamid = 0
    print("running")
    while identified == False:                                   #Loop solange kein Auto identifiziert ist
        print("startWhile")
        teamid = qr.readQRCode()                      #Wenn der Scan funktioniert hat, wird die teamid und ein True-Flag zurückgegeben
        if teamid != 0:
            identified = True                                  #Initialisiere Startsequenz sobald ein Auto erkannt wurde
            print("identified")
            x = time.time()
            rslt.showResults(0, teamid, x)             #zeigt bisherige Ergebnisse des Teams an
            #sound.playSound(-3)
            #sound.playSpeech(0, teamid)                          #erzählt infos zum Team
            fehlstart = lit.playStartSequence()                  #startet Ampel, Sounds und Fehlstartkontrolle
            if fehlstart:
                print("Fehlstart")
                break
            print("starttime")
            print(teamid)
            starttime = time.time()                                          #startet die Zeitmessung unabhängig davon, ob das Auto zu spät los fährt
    
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
    startProgramm()
except KeyboardInterrupt:
    print("Programm aborted")
    pass