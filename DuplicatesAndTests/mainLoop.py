import time
print("imported time")
import _thread
print("imported threading")
import checkpointLogic as cpl
print("imported checkpointlogic")
import sound
print("imported sound")
import light as lit
print("imported light")
import showResults as rslt
print("imported showResults")
#import runServer
#import readQRCode as qr

global identified
global activeCheckpoint

def startProgramm():
    identified = False
    print("running")
    while identified == False:                                   #Loop solange kein Auto identifiziert ist
        teamid=1
        #teamid, identified = qr.readQRCode()                     #Wenn der Scan funktioniert hat, wird die teamid und ein True-Flag zurückgegeben
        identified = True
        if identified == True:                                   #Initialisiere Startsequenz sobald ein Auto erkannt wurde
            print("identified")
            #rslt.showResults(0, teamid, time.time())             #zeigt bisherige Ergebnisse des Teams an
            #sound.playSpeech(0, teamid)                          #erzählt infos zum Team
            fehlstart = lit.playStartSequence()                  #startet Ampel, Sounds und Fehlstartkontrolle
            if fehlstart:
                print("Fehlstart")
                break
    print("starttime")
    starttime = time.clock()                                          #startet die Zeitmessung unabhängig davon, ob das Auto zu spät los fährt
    activeCheckpoint = 1
    
    while identified == True:                                                   #Loop für Rennen, Messung etc.
        print("starting Race")
        if cpl.checkpointReached(activeCheckpoint % 4):
            cpl.saveTime(starttime, activeCheckpoint % 4)                       #speichert die LiveZeit vom aktuellen Checkpoint [0,1,2,3]
            _thread.start_new_thread(lit.startLightExpress,(activeCheckpoint))  #Ampel leuchtet, checkpointabhängig, läuft parallel
            _thread.start_new_thread(sound.playSound,(activeCheckpoint))        #Spielt parallel den Sound, checkpointabhängig [1...8]
            #_thread.start_new_thread(sound.playSpeech,(activeCheckpoint, teamid)) #spricht (parallel),checkpointabhängig [1...8],teamid?
            rslt.showResults(activeCheckpoint, teamid, starttime)                #Zeigt Ergebnisse
            activeCheckpoint += 1
        if activeCheckpoint == 9:                                               #beendet das Rennen, speichert und zeigt Ergebnisse
            cpl.prepareDataForDB(teamID)                                        #rechnet einzelne Zeiten aus und schreibt diese in die DB
            rslt.showResults(9, teamid)
            lit.raceEnd()
            print("Rennen beendet")
            break
        
try:
    print("Starting Programm")
    startProgramm()
except KeyboardInterrupt:
    print("Programm aborted")
    pass